from datetime import date
from . import birth_mapper


def test_if_date_is_not_none_and_then_return_map_birth():
    assert birth_mapper.map_birth(date(1886, 1, 26), 'France') == {
        'month_day': '01-26', 'year': '1886', 'country': 'France'}


def test_if_date_is_none_and_then_return_map_birth():
    assert birth_mapper.map_birth(None, 'France') == {
        'month_day': None, 'year': None, 'country': 'France'}
