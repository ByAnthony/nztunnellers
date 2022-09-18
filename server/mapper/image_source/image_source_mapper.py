from ..date.date_mapper import assert_non_nullish_date_and_format


def map_author(authors):
    return [{'forename': row['author_forename'],
            'surname': row['author_surname']} for row in authors]


def map_image_source(image_source, image_authors):
    source = None
    for row in image_source:
        source = {
            'aucklandLibraries': row['image_source_auckland_libraries'],
            'archive': {'location': row['archives_name'], 'reference': row['archives_ref']},
            'family': row['family_name'],
            'newspaper': {'name': row['newspaper_name'], 'date': assert_non_nullish_date_and_format(row['newspaper_date'])},
            'book': {'author': map_author(image_authors), 'title': row['book_title'], 'town': row['book_town'], 'publisher': row['book_publisher'], 'year': row['book_year'], 'page': row['book_page']}
        }
    return source
