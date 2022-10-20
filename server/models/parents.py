from dataclasses import dataclass
from typing import Optional
from .parent import Parent


@dataclass
class Parents:
    mother: Parent
    father: Parent

    def get_parents(mother: Parent, father: Parent) -> dict[Optional[dict], Optional[dict]]:
        return {'mother': mother, 'father': father}
