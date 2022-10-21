from dataclasses import dataclass
from datetime import date
from typing import Optional
from .helpers.formatter_date import format_date, get_year


@dataclass
class BirthDetails:
    year: Optional[str]
    date: Optional[str]
    country: Optional[str]
