from datetime import date
from . import date_mapper


def test_if_date_is_not_none_and_then_format_date():
    assert date_mapper.assert_non_nullish_date_and_format(
        date(1886, 1, 26)) == '1886-01-26'


def test_if_date_is_none_and_then_return_none():
    assert date_mapper.assert_non_nullish_date_and_format(None) == None


def test_format_date_to_return_Y_m_d():
    assert date_mapper.format_date(date(1886, 1, 26)) == '1886-01-26'
