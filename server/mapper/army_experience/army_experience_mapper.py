from ..month_year.month_year_mapper import month_year_mapper


def map_army_experience(experience, lang):
    return [{'unit': row['army_experience_name'],
            'country': row['country'],
             'conflict': row['conflict_name'],
             'duration': month_year_mapper(row['army_experience_in_month'], lang)} for row in experience]
