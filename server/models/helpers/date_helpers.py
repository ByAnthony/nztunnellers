from datetime import date
from typing import Optional


def get_year(year: Optional[str], formatted_date: Optional[str]) -> Optional[str]:
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


def convert_month_year(month: Optional[int], lang: str) -> Optional[str]:
    mois = 'mois'
    month_col = {
        'en': 'month',
        'fr': mois
    }
    months_col = {
        'en': 'months',
        'fr': mois
    }
    years_col = {
        'en': 'years',
        'fr': 'ans'
    }

    if month is not None:
        if int(month) == 1:
            return '{} {}'.format(month, month_col[lang])
        if int(month) > int(1) and int(month) < int(24):
            return '{} {}'.format(month, months_col[lang])
        if int(month) >= int(24):
            result = int(month) // int(12)
            return '{} {}'.format(result, years_col[lang])
    return None
