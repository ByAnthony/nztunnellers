import time


def assert_non_nullish_date_and_format(date):
    if (date is not None):
        return format_date(date)


def format_date(date):
    return date.strftime('%Y-%m-%d')


def format_year(date_string):
    return date_string[0:4]


def format_month(date_string):
    return date_string[5:7]


def format_day(date_string):
    return date_string[8:10]
