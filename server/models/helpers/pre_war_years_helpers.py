from typing import Optional
from models.pre_war_years import ArmyExperience
from models.helpers.date_helpers import convert_month_year


def map_army_experience(experiences: list, lang: str) -> list[Optional[ArmyExperience]]:
    return [{'unit': row['army_experience_name'], 'country': row['country'], 'conflict': row['conflict_name'], 'duration': convert_month_year(row['army_experience_in_month'], lang)} for row in experiences]
