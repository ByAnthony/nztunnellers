from dataclasses import dataclass
from typing import Optional
from models.helpers.month_year_converter import convert_month_year


@dataclass
class ArmyExperience:
    unit: str
    country: Optional[str]
    conflict: Optional[str]
    duration: Optional[str]


@dataclass
class ArmyExperiences:
    experiences: list[ArmyExperience]

    def map_army_experience(experiences: tuple, lang: str) -> list[ArmyExperience]:
        return [{'unit': row['army_experience_name'], 'country': row['country'], 'conflict': row['conflict_name'], 'duration': convert_month_year(row['army_experience_in_month'], lang)} for row in experiences]
