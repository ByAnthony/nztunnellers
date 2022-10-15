import time
from datetime import date


def assert_non_nullish_date_and_format(date: date) -> str:
    if date is not None:
        return format_date(date)


def format_date(date: date) -> str:
    return date.strftime('%Y-%m-%d')


def format_year(date: str) -> str:
    if date is not None:
        return date[0:4]
