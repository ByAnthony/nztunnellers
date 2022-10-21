from models.army_experiences import ArmyExperience
from models.helpers.formatter_date import convert_month_year


def map_army_experience(experiences: list, lang: str) -> list[ArmyExperience]:
    return [{'unit': row['army_experience_name'], 'country': row['country'], 'conflict': row['conflict_name'], 'duration': convert_month_year(row['army_experience_in_month'], lang)} for row in experiences]
