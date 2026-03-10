from datetime import datetime
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.enums import LightIntensity, PlantDensity


class Aquarium(Base):
    __tablename__ = "aquariums"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    volume_liters: Mapped[int] = mapped_column(Integer, nullable=False)

    co2_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False)
    light_intensity: Mapped[LightIntensity] = mapped_column(
        Enum(LightIntensity, name="light_intensity_enum"),
        nullable=False,
    )
    light_duration_hours: Mapped[int] = mapped_column(
        Integer, nullable=False, default=8
    )
    plant_density: Mapped[PlantDensity] = mapped_column(
        Enum(PlantDensity, name="plant_density_enum"),
        nullable=False,
    )

    water_change_interval_weeks: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    water_change_percent: Mapped[float | None] = mapped_column(
        Numeric(5, 2), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    user: Mapped["User"] = relationship(back_populates="aquariums")
    target_profile: Mapped["TargetProfile | None"] = relationship(
        back_populates="aquarium",
        uselist=False,
        cascade="all, delete-orphan",
    )
    calculations: Mapped[list["Calculation"]] = relationship(
        back_populates="aquarium",
        cascade="all, delete-orphan",
    )
    measurements: Mapped[list["Measurement"]] = relationship(
        back_populates="aquarium",
        cascade="all, delete-orphan",
    )
    dosing_logs: Mapped[list["DosingLog"]] = relationship(
        back_populates="aquarium",
        cascade="all, delete-orphan",
    )
    water_change_logs: Mapped[list["WaterChangeLog"]] = relationship(
        back_populates="aquarium",
        cascade="all, delete-orphan",
    )
