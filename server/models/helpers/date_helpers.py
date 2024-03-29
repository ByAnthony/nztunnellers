# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from ..date import Date


def format_date_to_year(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[0:4]
    return None


def format_date_to_month(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[5:7]
    return None


def format_date_to_day(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[8:10]
    return None


def format_date_to_day_and_month(date: Optional[str], lang: str) -> Optional[str]:
    months = {
        "1": {"en": "January", "fr": "janvier"},
        "2": {"en": "February", "fr": "février"},
        "3": {"en": "March", "fr": "mars"},
        "4": {"en": "April", "fr": "avril"},
        "5": {"en": "May", "fr": "mai"},
        "6": {"en": "June", "fr": "juin"},
        "7": {"en": "July", "fr": "juillet"},
        "8": {"en": "August", "fr": "août"},
        "9": {"en": "September", "fr": "septembre"},
        "10": {"en": "October", "fr": "octobre"},
        "11": {"en": "November", "fr": "novembre"},
        "12": {"en": "December", "fr": "décembre"},
    }
    if date is not None:
        month = format_date_to_month(date)
        day = format_date_to_day(date)
        if month is not None and day is not None:
            strip_month = month.lstrip("0")
            strip_day = day.lstrip("0")
            no_break_space = "\N{NO-BREAK SPACE}"
            return f"{strip_day}{no_break_space}{months[strip_month][lang]}"
    return None


def format_date_to_day_month_and_year(date: Optional[str], lang: str) -> Optional[str]:
    if date is not None:
        return f"{format_date_to_day_and_month(date, lang)} {format_date_to_year(date)}"
    return None


def format_date_string_to_date_type(
    year: Optional[str], date: Optional[str], lang: str
) -> Optional[Date]:
    if year is None and date is None:
        return None
    if year is None and date is not None:
        return None
    return Date(year, format_date_to_day_and_month(date, lang))


def get_full_date(date: str, lang: str) -> Date:
    return Date(format_date_to_year(date), format_date_to_day_and_month(date, lang))


def get_optional_date(date: Optional[str], lang: str) -> Optional[Date]:
    if date is not None:
        return get_full_date(date, lang)
    return None


def convert_month_in_duration(month: Optional[str], lang: str) -> Optional[str]:
    if month is not None:
        mois = "mois"
        month_col = {"en": "month", "fr": mois}
        months_col = {"en": "months", "fr": mois}
        years_col = {"en": "years", "fr": "ans"}
        no_break_space = "\N{NO-BREAK SPACE}"
        if int(month) == 1:
            return f"{month}{no_break_space}{month_col[lang]}"
        elif int(month) > int(1) and int(month) < int(24):
            return f"{month}{no_break_space}{months_col[lang]}"
        else:
            result = int(month) // int(12)
            return f"{result}{no_break_space}{years_col[lang]}"
    return None


def convert_immigration_duration_to_arrival_year(
    month: Optional[str], enlistment_date: Optional[str]
) -> Optional[str]:
    if month is not None:
        if int(month) < 12:
            return format_date_to_year(enlistment_date)
        if int(month) >= 12:
            enlistment_year = format_date_to_year(enlistment_date)
            residence_year = int(month) / 12
            if enlistment_year is not None:
                return str(int(enlistment_year) - int(residence_year))
    return None


def calculate_age_with_full_date(date_1: str, date_2: str) -> int:
    first_date = datetime.datetime.strptime(date_1, "%Y-%m-%d")
    second_date = datetime.datetime.strptime(date_2, "%Y-%m-%d")
    age = second_date.year - first_date.year
    if second_date.month < first_date.month or (
        second_date.month == first_date.month and second_date.day < first_date.day
    ):
        age -= 1
    return age


def calculate_age_with_years(date_1: str, date_2: str) -> int:
    age = int(date_2) - int(date_1)
    return age
