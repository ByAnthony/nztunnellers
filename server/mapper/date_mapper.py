import time


def map_birth(year, country):
    return {'year': year, 'country': country}


def format_year(date):
    return date.strftime('%Y')


def format_date(date):
    return date.strftime('%Y-%m-%d')
