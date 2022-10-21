from dataclasses import dataclass
from typing import Optional
from models.employment import Employment
from models.army_experience_list import ArmyExperiences


@dataclass
class PreWarYear:
    marital_status: Optional[str]
    wife: Optional[str]
    employment: Employment
    residence: Optional[str]
    religion: Optional[str]
    army_experience: ArmyExperiences
