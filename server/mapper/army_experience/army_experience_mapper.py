from ..month_year.month_year_mapper import convert_month_year


def map_army_experience(experience, lang):
    print(experience)
    return [{'unit': row['army_experience_name'],
            'country': row['country'],
             'conflict': row['conflict_name'],
             'duration': convert_month_year(row['army_experience_in_month'], lang)} for row in experience]
