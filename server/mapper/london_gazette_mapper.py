from mapper.date_mapper import assert_non_nullish_date_and_format


def map_london_gazette(date, page):
    if (date is not None and page is not None):
        return [
            {'date': assert_non_nullish_date_and_format(
                date), 'page': page}
        ]
    return None
