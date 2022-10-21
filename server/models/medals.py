from dataclasses import dataclass
from typing import Optional


@dataclass
class Medal:
    name: str
    citation: Optional[str]
    country: str


@dataclass
class Medals:
    medals: list[Medal]

    def map_medals(medals: tuple) -> list[Medal]:
        return [{'name': row['medal_name'], 'citation': row['medal_citation'], 'country': row['country']} for row in medals]
