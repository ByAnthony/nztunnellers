from dataclasses import dataclass
from typing import Optional
from models.helpers.month_year_converter import convert_month_year


class ArmyExperienceList:

    def map_army_experience(experience: tuple, lang: str) -> list[Optional[dict[Optional[str], Optional[str], Optional[str], Optional[str]]]]:
        return [
            {
                'unit': row['army_experience_name'],
                'country': row['country'],
                'conflict': row['conflict_name'],
                'duration': convert_month_year(row['army_experience_in_month'], lang)
            }
            for row in experience
        ]
