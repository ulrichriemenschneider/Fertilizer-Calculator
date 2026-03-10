from sqlalchemy import String, ForeignKey, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.enums import FertilizerType, NutrientCode


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    systems: Mapped[list["FertilizerSystem"]] = relationship(
        back_populates="manufacturer",
        cascade="all, delete-orphan",
    )


class FertilizerSystem(Base):
    __tablename__ = "fertilizer_systems"

    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="systems")
    fertilizers: Mapped[list["Fertilizer"]] = relationship(
        back_populates="system",
        cascade="all, delete-orphan",
    )


class Fertilizer(Base):
    __tablename__ = "fertilizers"

    id: Mapped[int] = mapped_column(primary_key=True)
    system_id: Mapped[int] = mapped_column(
        ForeignKey("fertilizer_systems.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    fertilizer_type: Mapped[FertilizerType] = mapped_column(
        Enum(FertilizerType, name="fertilizer_type_enum"),
        nullable=False,
    )

    reference_ml: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    reference_liters: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    system: Mapped["FertilizerSystem"] = relationship(back_populates="fertilizers")
    nutrients: Mapped[list["FertilizerNutrient"]] = relationship(
        back_populates="fertilizer",
        cascade="all, delete-orphan",
    )


class FertilizerNutrient(Base):
    __tablename__ = "fertilizer_nutrients"

    id: Mapped[int] = mapped_column(primary_key=True)
    fertilizer_id: Mapped[int] = mapped_column(
        ForeignKey("fertilizers.id", ondelete="CASCADE"),
        nullable=False,
    )
    nutrient_code: Mapped[NutrientCode] = mapped_column(
        Enum(NutrientCode, name="nutrient_code_enum"),
        nullable=False,
    )

    # Erhöhung in mg/l bezogen auf reference_ml und reference_liters
    increase_mg_l: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

    fertilizer: Mapped["Fertilizer"] = relationship(back_populates="nutrients")
