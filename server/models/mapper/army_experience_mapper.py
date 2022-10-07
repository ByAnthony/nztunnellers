from ..converter.month_year_converter import convert_month_year


def map_army_experience(experience, lang):
    return [
        {
            'unit': row['army_experience_name'],
            'country': row['country'],
            'conflict': row['conflict_name'],
            'duration': convert_month_year(row['army_experience_in_month'], lang)
        }
        for row in experience
    ]
