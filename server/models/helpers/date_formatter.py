import time
from datetime import date
from typing import Optional


def get_year(year: Optional[str], formatted_date: str) -> str:
    if year is not None:
        return year
    else:
        formatted_year = format_year(formatted_date)
        return formatted_year


def format_date(date: Optional[date]) -> str:
    if date is not None:
        return date.strftime('%Y-%m-%d')


def format_year(date: str) -> str:
    if date is not None:
        return date[0:4]
