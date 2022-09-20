def map_authors(authors):
    return [{'forename': row['author_forename'],
            'surname': row['author_surname']} for row in authors]
