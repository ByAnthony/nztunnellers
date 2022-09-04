import time


def assert_non_nullish_date(date):
    if (date is not None):
        return format_date(date)


def format_year(date):
    return date.strftime('%Y')


def format_month_day(date):
    return date.strftime('%m-%d')


def format_date(date):
    return date.strftime('%Y-%m-%d')
