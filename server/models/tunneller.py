from dataclasses import dataclass
from datetime import date
from .roll import Roll

from .formatter.birth_formatter import format_birth
from .formatter.parent_formatter import format_parent


@dataclass
class Tunneller(Roll):
    origins: dict

    def get_origins(
        birth_year: date.year,
        birth_date: date,
        birth_country: str,
        mother: str,
        mother_origin: str,
        father: str,
        father_origin: str
    ):
        return {
            'birth': format_birth(birth_year, birth_date, birth_country),
            'parents': {'mother': format_parent(mother, mother_origin),
                        'father': format_parent(father, father_origin)}
        }
