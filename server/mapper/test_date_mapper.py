from date_mapper import format_date
from datetime import date


def test_date():
    assert format_date(date(2022, 9, 9)) == '2022-09-09'
