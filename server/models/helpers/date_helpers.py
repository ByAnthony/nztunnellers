from datetime import date
import locale
from typing import Optional


def get_birth_year(year: Optional[str], formatted_date: Optional[str]) -> Optional[str]:
    if year is not None:
        return year
    else:
        if formatted_date is not None:
            formatted_year = format_year(formatted_date)
            return formatted_year
        return None


def format_date(date: Optional[date]) -> Optional[str]:
    if date is not None:
        return date.strftime('%Y-%m-%d')
    return None


def format_year(date: str) -> str:
    if date is not None:
        return date[0:4]


def find_month(date: str) -> str:
    return date[5:7]


def find_day(date: str) -> str:
    return date[8:10]


def format_to_day_and_month(date: Optional[date], lang) -> Optional[str]:
    months = {'1': 'January', '2': 'Feburary', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
              '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    mois = {'1': 'janvier', '2': 'février', '3': 'mars', '4': 'avril', '5': 'mai', '6': 'juin',
            '7': 'juillet', '8': 'août', '9': 'septembre', '10': 'octobre', '11': 'novembre', '12': 'décembre'}

    if date is not None:
        formatted_date = format_date(date)
        month = find_month(formatted_date).lstrip('0')
        day = find_day(formatted_date).lstrip('0')
        no_break_space = '\N{NO-BREAK SPACE}'

        if lang == 'en':
            return '{}{}{}'.format(day, no_break_space, months.get(month))
        elif lang == 'fr':
            return '{}{}{}'.format(day, no_break_space, mois.get(month))
    else:
        return None


def format_to_day_month_and_year(date: Optional[date], lang) -> Optional[str]:
    if date is not None:
        return format_to_day_and_month(date, lang) + ' ' + format_year(format_date(date))
    return None


def convert_month_year(month: Optional[int], lang: str) -> Optional[str]:
    mois = 'mois'
    month_col = {'en': 'month', 'fr': mois}
    months_col = {'en': 'months', 'fr': mois}
    years_col = {'en': 'years', 'fr': 'ans'}
    no_break_space = '\N{NO-BREAK SPACE}'

    if month is not None:
        if int(month) == 1:
            return '{}{}{}'.format(month, no_break_space, month_col[lang])
        if int(month) > int(1) and int(month) < int(24):
            return '{}{}{}'.format(month, no_break_space, months_col[lang])
        if int(month) >= int(24):
            result = int(month) // int(12)
            return '{}{}{}'.format(result, no_break_space, years_col[lang])
    return None
