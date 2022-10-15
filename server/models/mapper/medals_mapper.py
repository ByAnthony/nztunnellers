def map_medals(medals: tuple) -> list[dict]:
    return [{'name': row['medal_name'], 'citation': row['medal_citation'], 'country': row['country']} for row in medals]
