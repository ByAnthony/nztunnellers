from mapper.date_mapper import format_month_day, format_year


def map_birth(date, country):
    year = format_year(date)
    month_day = format_month_day(date)
    return {'month_day': month_day, 'year': year, 'country': country}
