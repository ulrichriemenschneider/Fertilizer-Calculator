import enum


class LightIntensity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class PlantDensity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class DosingInterval(str, enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"


class FertilizerType(str, enum.Enum):
    MACRO_N = "macro_n"
    MACRO_P = "macro_p"
    MACRO_K = "macro_k"
    MICRO_FE = "micro_fe"
    ALL_IN_ONE = "all_in_one"
    SPECIAL = "special"


class NutrientCode(str, enum.Enum):
    NO3 = "NO3"
    PO4 = "PO4"
    K = "K"
    FE = "FE"
