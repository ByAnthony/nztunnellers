from dataclasses import dataclass
from typing import Optional


@dataclass()
class ArmyExperience:
    unit: Optional[str]
    country: Optional[str]
    conflict: Optional[str]
    duration: Optional[str]
