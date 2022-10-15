from datetime import date
from ....models.formatter import date_formatter


def test_if_date_is_not_none_and_then_format_date():
    assert date_formatter.assert_non_nullish_date_and_format(
        date(1886, 1, 26)) == '1886-01-26'


def test_if_date_is_none_and_then_return_none():
    assert date_formatter.assert_non_nullish_date_and_format(None) == None


def test_format_date_to_return_Y_m_d():
    assert date_formatter.format_date(date(1886, 1, 26)) == '1886-01-26'


def test_format_year():
    assert date_formatter.format_year('1886-01-26') == '1886'
