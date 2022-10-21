from datetime import date
from server.models.helpers import formatter_date


def test_format_date_to_return_Y_m_d():
    assert formatter_date.format_date(date(1886, 1, 26)) == '1886-01-26'


def test_format_year():
    assert formatter_date.format_year('1886-01-26') == '1886'
