from mapper.date.date_mapper import assert_non_nullish_date_and_format


def map_london_gazette(london_gazette):
    return [{'date': assert_non_nullish_date_and_format(row['london_gazette_date']),
            'page': row['london_gazette_page']} for row in london_gazette]
