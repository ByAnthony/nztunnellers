def map_medals(medals):
    return [{'name': row['medal_name_en'], 'citation': row['medal_citation_en'], 'country': row['country_en']} for row in medals]
