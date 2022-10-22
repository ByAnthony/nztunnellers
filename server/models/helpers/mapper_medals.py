from models.military_years import Medal


def map_medals(medals: tuple) -> list[Medal]:
    return [{'name': row['medal_name'], 'citation': row['medal_citation'], 'country': row['country']} for row in medals]
