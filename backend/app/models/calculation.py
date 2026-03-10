from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Enum, Numeric, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.enums import DosingInterval


class TargetProfile(Base):
    __tablename__ = "target_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    aquarium_id: Mapped[int] = mapped_column(
        ForeignKey("aquariums.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    no3: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=15.0)
    po4: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0.50)
    k: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=10.0)
    fe: Mapped[float] = mapped_column(Numeric(10, 3), nullable=False, default=0.05)

    aquarium: Mapped["Aquarium"] = relationship(back_populates="target_profile")


class Calculation(Base):
    __tablename__ = "calculations"

    id: Mapped[int] = mapped_column(primary_key=True)
    aquarium_id: Mapped[int] = mapped_column(
        ForeignKey("aquariums.id", ondelete="CASCADE"),
        nullable=False,
    )

    dosing_interval: Mapped[DosingInterval] = mapped_column(
        Enum(DosingInterval, name="dosing_interval_enum"),
        nullable=False,
    )

    input_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    result_data: Mapped[dict] = mapped_column(JSON, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    aquarium: Mapped["Aquarium"] = relationship(back_populates="calculations")


class Measurement(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(primary_key=True)
    aquarium_id: Mapped[int] = mapped_column(
        ForeignKey("aquariums.id", ondelete="CASCADE"),
        nullable=False,
    )

    no3: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    po4: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    k: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    fe: Mapped[float | None] = mapped_column(Numeric(10, 3), nullable=True)

    measured_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    aquarium: Mapped["Aquarium"] = relationship(back_populates="measurements")


class DosingLog(Base):
    __tablename__ = "dosing_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    aquarium_id: Mapped[int] = mapped_column(
        ForeignKey("aquariums.id", ondelete="CASCADE"),
        nullable=False,
    )
    fertilizer_id: Mapped[int] = mapped_column(
        ForeignKey("fertilizers.id", ondelete="CASCADE"),
        nullable=False,
    )

    amount_ml: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    dosed_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    aquarium: Mapped["Aquarium"] = relationship(back_populates="dosing_logs")
    fertilizer: Mapped["Fertilizer"] = relationship()


class WaterChangeLog(Base):
    __tablename__ = "water_change_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    aquarium_id: Mapped[int] = mapped_column(
        ForeignKey("aquariums.id", ondelete="CASCADE"),
        nullable=False,
    )

    changed_percent: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    changed_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    aquarium: Mapped["Aquarium"] = relationship(back_populates="water_change_logs")
