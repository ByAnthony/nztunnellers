from ..date.date_mapper import assert_non_nullish_date_and_format


def map_birth(date, year, country):
    formatted_birth_date = assert_non_nullish_date_and_format(date)
    return {'date': formatted_birth_date, 'year': year, 'country': country}
