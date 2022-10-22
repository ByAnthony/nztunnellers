from dataclasses import dataclass
from typing import Optional


@dataclass()
class ArmyExperience:
    unit: Optional[str]
    country: Optional[str]
    conflict: Optional[str]
    duration: Optional[str]


@dataclass
class Employment:
    occupation: str
    employer: Optional[str]


@dataclass
class PreWarYear:
    marital_status: Optional[str]
    wife: Optional[str]
    employment: Employment
    residence: Optional[str]
    religion: Optional[str]
    army_experience: list[Optional[ArmyExperience]]
