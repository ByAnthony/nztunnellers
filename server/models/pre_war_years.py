from dataclasses import dataclass
from typing import Optional
from models.employment import Employment
from models.army_experience_list import ArmyExperienceList


@dataclass
class PreWarYear:
    marital_status: Optional[str]
    wife: Optional[str]
    employment: Employment
    residence: Optional[str]
    religion: Optional[str]
    army_experience: ArmyExperienceList

    def get_pre_war_years(marital_status: Optional[str], wife: Optional[str], employment: Employment, residence: Optional[str], religion: Optional[str], army_experience: ArmyExperienceList) -> dict[Optional[str], Optional[str], Employment, Optional[str], Optional[str], ArmyExperienceList]:
        return {'marital_status': marital_status, 'wife': wife, 'employment': employment, 'residence': residence, 'religion': religion, 'army_experience': army_experience}
