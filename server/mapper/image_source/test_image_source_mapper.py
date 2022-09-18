from . import image_source_mapper

author_1 = {'author_forename': 'Arthur Conan', 'author_surname': 'Doyle'}
author_2 = {'author_forename': 'Mary', 'author_surname': 'Shelley'}


def test_map_one_author():
    assert image_source_mapper.map_authors((author_1,)) == [
        {'forename': 'Arthur Conan', 'surname': 'Doyle'}]


def test_map_multiple_authors():
    assert image_source_mapper.map_authors((author_1, author_2)) == [
        {'forename': 'Arthur Conan', 'surname': 'Doyle'}, {'forename': 'Mary', 'surname': 'Shelley'}]


# def map_image_source(image_source, image_authors):
#     source = None
#     for row in image_source:
#         source = {
#             'aucklandLibraries': row['image_source_auckland_libraries'],
#             'archive': {'location': row['archives_name'], 'reference': row['archives_ref']},
#             'family': row['family_name'],
#             'newspaper': {'name': row['newspaper_name'], 'date': assert_non_nullish_date_and_format(row['newspaper_date'])},
#             'book': {'author': map_author(image_authors), 'title': row['book_title'], 'town': row['book_town'], 'publisher': row['book_publisher'], 'year': row['book_year'], 'page': row['book_page']}
#         }
#     return source
