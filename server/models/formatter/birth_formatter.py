from .date_formatter import assert_non_nullish_date_and_format, format_year


def format_birth(date, year, country):

    formatted_birth_date = assert_non_nullish_date_and_format(date)
    formatted_year = format_year(formatted_birth_date)

    def get_birth_year(year, formatted_year):
        if year is not None:
            return year
        else:
            return formatted_year

    return {'date': formatted_birth_date, 'year': get_birth_year(year, formatted_year), 'country': country}
