# -*- coding: utf-8 -*-
from datetime import date
from typing import Optional


def get_birth_year(year: Optional[str], formatted_date: Optional[str]) -> Optional[str]:
    if year is not None:
        return year
    else:
        if formatted_date is not None:
            formatted_year = format_year(formatted_date)
            if formatted_year is not None:
                return formatted_year


def format_date(date: Optional[date]) -> Optional[str]:
    if date is not None:
        return date.strftime("%Y-%m-%d")
    return None


def format_year(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[0:4]
    return None


def find_month(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[5:7]
    return None


def find_day(date: Optional[str]) -> Optional[str]:
    if date is not None:
        return date[8:10]
    return None


def format_to_day_and_month(date: Optional[date], lang: str) -> Optional[str]:
    def strip_zero(string: str) -> str:
        return string.lstrip("0")

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
    formatted_date = format_date(date)
    month = find_month(formatted_date)
    day = find_day(formatted_date)
    no_break_space = "\N{NO-BREAK SPACE}"

    if month is not None and day is not None:
        return "{}{}{}".format(
            strip_zero(day), no_break_space, strip_zero(months[month][lang])
        )
    return None


def format_to_day_month_and_year(date: Optional[date], lang: str) -> Optional[str]:
    formatted_day_month = format_to_day_and_month(date, lang)
    formatted_year = format_year(format_date(date))

    if formatted_day_month is not None and formatted_year is not None:
        return "{} {}".format(formatted_day_month, formatted_year)
    return None


def convert_month_year(month: Optional[int], lang: str) -> Optional[str]:
    if month is not None:
        mois = "mois"
        month_col = {"en": "month", "fr": mois}
        months_col = {"en": "months", "fr": mois}
        years_col = {"en": "years", "fr": "ans"}
        no_break_space = "\N{NO-BREAK SPACE}"

        if int(month) == 1:
            return "{}{}{}".format(month, no_break_space, month_col[lang])
        elif int(month) > int(1) and int(month) < int(24):
            return "{}{}{}".format(month, no_break_space, months_col[lang])
        else:
            result = int(month) // int(12)
            return "{}{}{}".format(result, no_break_space, years_col[lang])
    return None
