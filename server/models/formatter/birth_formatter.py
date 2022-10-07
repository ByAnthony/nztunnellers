from .date_formatter import assert_non_nullish_date_and_format, format_year


def format_birth(year, date, country):

    formatted_birth_date = assert_non_nullish_date_and_format(date)

    def get_birth_year(birth_year, formatted_birth_date):
        if birth_year is not None:
            return birth_year
        else:
            formatted_year = format_year(formatted_birth_date)
            return formatted_year

    return {
        'year': get_birth_year(year, formatted_birth_date),
        'date': formatted_birth_date,
        'country': country
    }
