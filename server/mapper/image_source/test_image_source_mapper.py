from datetime import date
from . import image_source_mapper

author_1 = {'author_forename': 'Arthur Conan', 'author_surname': 'Doyle'}
author_2 = {'author_forename': 'Mary', 'author_surname': 'Shelley'}
image_source_data = {'image_source_auckland_libraries': '31-B2671', 'archives_name': 'Archives New Zealand', 'archives_ref': 'AABK 188805', 'family_name': 'Hopkins', 'newspaper_name': 'Dunedin News',
                     'newspaper_date': date(1918, 11, 12), 'book_title': 'Amazing Story of the Tunnellers', 'book_town': 'Hamilton', 'book_publisher': 'Publisher And Co.', 'book_year': '1932', 'book_page': 123}


def test_map_one_author():
    assert image_source_mapper.map_authors((author_1,)) == [
        {'forename': 'Arthur Conan', 'surname': 'Doyle'}]


def test_map_multiple_authors():
    assert image_source_mapper.map_authors((author_1, author_2)) == [
        {'forename': 'Arthur Conan', 'surname': 'Doyle'}, {'forename': 'Mary', 'surname': 'Shelley'}]


def test_map_image_source_for_auckland_libraries():
    assert image_source_mapper.map_image_source((image_source_data,), (author_2,)) == {
        'archives': {'location': 'Archives New Zealand', 'reference': 'AABK 188805'},
        'aucklandLibraries': '31-B2671',
        'book': {'authors': image_source_mapper.map_authors((author_2,)), 'page': 123, 'publisher': 'Publisher And Co.', 'title': 'Amazing Story of the Tunnellers', 'town': 'Hamilton', 'year': '1932'},
        'family': 'Hopkins',
        'newspaper': {'name': 'Dunedin News', 'date': '1918-11-12'}
    }
