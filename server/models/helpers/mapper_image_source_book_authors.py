def map_authors(authors: tuple) -> list[dict]:
    return [{'forename': row['author_forename'],
            'surname': row['author_surname']} for row in authors]
