import time
from datetime import date


def format_date(date: date or None) -> str:
    if date is not None:
        return date.strftime('%Y-%m-%d')


def format_year(date: str) -> str:
    if date is not None:
        return date[0:4]
