import time
from datetime import date


def get_year(year: str or None, formatted_date: str) -> str:
    if year is not None:
        return year
    else:
        formatted_year = format_year(formatted_date)
        return formatted_year


def format_date(date: date or None) -> str:
    if date is not None:
        return date.strftime('%Y-%m-%d')


def format_year(date: str) -> str:
    if date is not None:
        return date[0:4]
