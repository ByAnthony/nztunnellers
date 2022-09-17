from ..date.date_mapper import assert_non_nullish_date_and_format


def map_image_source(image_source):
    source = None
    for row in image_source:
        source = {
            'auckland_libraries': row['image_source_auckland_libraries'],
            'archive': {'location': row['archives_name'], 'reference': row['archives_ref']},
            'family': row['family_name'],
            'newspaper': {'name': row['newspaper_name'], 'date': assert_non_nullish_date_and_format(row['newspaper_date'])}
        }
    return source
