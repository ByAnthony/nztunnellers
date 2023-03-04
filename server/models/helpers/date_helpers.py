# -*- coding: utf-8 -*-
from typing import Optional

from ..date import Date


def format_date_to_birth_year(
    year: Optional[str], formatted_date: Optional[str]
) -> Optional[str]:
    if year is not None:
        return year
    else:
        if formatted_date is not None:
            formatted_year = format_date_to_year(formatted_date)
            return formatted_year
    return None


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

            return "{}{}{}".format(strip_day, no_break_space, months[strip_month][lang])

    return None


def format_date_to_day_month_and_year(date: Optional[str], lang: str) -> Optional[str]:
    if date is not None:
        return "{} {}".format(
            format_date_to_day_and_month(date, lang), format_date_to_year(date)
        )
    return None


def get_birth_date(year: Optional[str], date: Optional[str], lang: str) -> Date:
    return Date(
        format_date_to_birth_year(year, date), format_date_to_day_and_month(date, lang)
    )


def get_date(date: Optional[str], lang: str) -> Optional[Date]:
    if date is not None:
        return Date(format_date_to_year(date), format_date_to_day_and_month(date, lang))
    return None


def convert_month_year(month: Optional[str], lang: str) -> Optional[str]:
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


def convert_immigration_year(
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
