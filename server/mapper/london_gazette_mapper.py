from mapper.date_mapper import assert_non_nullish_date_and_format


def map_london_gazette(date_1, page_1, date_2, page_2, date_3, page_3, date_4, page_4):
    if (date_4 is not None):
        return [
            {'date': assert_non_nullish_date_and_format(
                date_1), 'page': page_1},
            {'date': assert_non_nullish_date_and_format(
                date_2), 'page': page_2},
            {'date': assert_non_nullish_date_and_format(
                date_3), 'page': page_3},
            {'date': assert_non_nullish_date_and_format(
                date_4), 'page': page_4}
        ]
    elif (date_3 is not None and date_4 is None):
        return [
            {'date': assert_non_nullish_date_and_format(
                date_1), 'page': page_1},
            {'date': assert_non_nullish_date_and_format(
                date_2), 'page': page_2},
            {'date': assert_non_nullish_date_and_format(
                date_3), 'page': page_3}
        ]
    elif (date_2 is not None and date_3 is None):
        return [
            {'date': assert_non_nullish_date_and_format(
                date_1), 'page': page_1},
            {'date': assert_non_nullish_date_and_format(
                date_2), 'page': page_2}
        ]
    elif (date_1 is not None and date_2 is None):
        return [
            {'date': assert_non_nullish_date_and_format(
                date_1), 'page': page_1}
        ]
