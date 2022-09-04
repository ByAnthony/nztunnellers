from mapper.date_mapper import assert_non_nullish_date, format_month_day, format_year


def map_birth(date, country):
    non_nullish_date = assert_non_nullish_date(date)

    if (non_nullish_date is not None):
        year = format_year(non_nullish_date)
        month_day = format_month_day(non_nullish_date)
        return {'month_day': month_day, 'year': year, 'country': country}
    else:
        return {'month_day': None, 'year': None, 'country': country}
