def map_medals(medals):
    return [{'name': row['medal_name'], 'citation': row['medal_citation'], 'country': row['country']} for row in medals]
