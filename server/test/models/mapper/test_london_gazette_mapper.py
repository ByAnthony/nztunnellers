from datetime import date
from ....mapper.mapper import london_gazette_mapper


london_gazette_list = ({'london_gazette_date': date(1917, 12, 28), 'london_gazette_page': '13575'}, {
    'london_gazette_date': date(1918, 1, 1), 'london_gazette_page': '29'})


def test_if_london_gazette_is_not_none_then_returns_map_london_gazette():
    assert london_gazette_mapper.map_london_gazette(london_gazette_list) == [
        {
            "date": "1917-12-28",
            "page": "13575"
        },
        {
            "date": "1918-01-01",
            "page": "29"
        }
    ]


def test_if_london_gazette_is_none_then_returns_empty_list():
    assert london_gazette_mapper.map_london_gazette(()) == []
