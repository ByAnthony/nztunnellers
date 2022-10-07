from dataclasses import dataclass
from datetime import date
from .roll import Roll

from .formatter.date_formatter import assert_non_nullish_date_and_format, format_year


@dataclass
class Tunneller(Roll):
    origins: dict

    def get_birth(birth_year, birth_date, birth_country):

        formatted_birth_date = assert_non_nullish_date_and_format(birth_date)

        def get_birth_year(birth_year, formatted_birth_date):
            if birth_year is not None:
                return birth_year
            else:
                formatted_year = format_year(formatted_birth_date)
                return formatted_year

        return {
            'year': get_birth_year(birth_year, formatted_birth_date),
            'date': formatted_birth_date,
            'country': birth_country
        }

    def get_parent(name, origin_country):
        return {
            'name': name,
            'origin': origin_country
        }

    def get_origins(
        birth: dict,
        mother: dict,
        father: dict
    ):
        return {
            'birth': birth,
            'parents': {
                'mother': mother,
                'father': father
            }
        }
