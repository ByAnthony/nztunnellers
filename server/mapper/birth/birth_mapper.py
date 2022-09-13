from ..date.date_mapper import format_date, format_day, format_month, format_year


def map_birth(date, year, country):
    if (date is not None):
        formatted_birth_date = format_date(date)
        return {'date': formatted_birth_date, 'year': None, 'country': country}
    return {'date': None, 'year': year, 'country': country}
