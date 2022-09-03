import time


def map_birth(date, country):
    year = format_year(date)
    month_day = format_month_day(date)
    return {'month_day': month_day, 'year': year, 'country': country}


def format_year(date):
    return date.strftime('%Y')


def format_month_day(date):
    return date.strftime('%m-%d')


def format_date(date):
    return date.strftime('%Y-%m-%d')
