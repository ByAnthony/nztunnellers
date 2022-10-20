from dataclasses import dataclass
from datetime import date
from typing import Optional
from .formatter.date_formatter import format_date, get_year


@dataclass
class BirthDetails:
    birth_year: Optional[str]
    birth_date: Optional[str]
    birth_country: Optional[str]

    def get_birth_details(year: Optional[str], date: Optional[date], country: Optional[str]) -> dict[Optional[str], Optional[str], Optional[str]]:
        birth_date = format_date(date)
        birth_year = get_year(year, birth_date)
        return {'year': birth_year, 'date': birth_date, 'country': country}
