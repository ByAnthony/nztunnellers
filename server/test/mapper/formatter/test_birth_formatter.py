from datetime import date
from ....mapper.formatter import birth_formatter


def test_if_date_and_copuntry_are_not_none_and_year_is_none_then_return_map_birth():
    assert birth_formatter.format_birth(date(1886, 1, 26), None, 'France') == {
        'date': '1886-01-26', 'year': None, 'country': 'France'}


def test_if_date_is_none_and_year_and_country_are_not_none_then_return_map_birth():
    assert birth_formatter.format_birth(None, '1886', 'France') == {
        'date': None, 'year': '1886', 'country': 'France'}


def test_if_date_is_not_none_and_year_and_country_are_none_then_return_map_birth():
    assert birth_formatter.format_birth(date(1886, 1, 26), None, None) == {
        'date': '1886-01-26', 'year': None, 'country': None}


def test_if_date_and_country_are_none_and_year_is_not_none_then_return_map_birth():
    assert birth_formatter.format_birth(None, '1886', None) == {
        'date': None, 'year': '1886', 'country': None}
