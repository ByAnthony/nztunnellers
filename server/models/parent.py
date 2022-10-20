from dataclasses import dataclass
from typing import Optional


@dataclass
class Parent:
    name: Optional[str]
    origin_country: Optional[str]

    def get_parent(name: Optional[str], country: Optional[str]) -> dict[Optional[str], Optional[str]]:
        if name and country is not None:
            return {'name': name, 'origin': country}
        return None
