import time


def assert_non_nullish_date(date):
    if (date is not None):
        return format_date(date)


def format_year(string):
    return string[0:4]


def format_month_day(string):
    return string[5:10]


def format_date(date):
    return date.strftime('%Y-%m-%d')
