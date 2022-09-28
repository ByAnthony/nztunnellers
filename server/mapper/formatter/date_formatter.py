import time


def assert_non_nullish_date_and_format(date):
    if (date is not None):
        return format_date(date)


def format_date(date):
    return date.strftime('%Y-%m-%d')
