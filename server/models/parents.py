from dataclasses import dataclass
from typing import Optional
from .parent import Parent


@dataclass
class Parents:
    mother: Parent
    father: Parent

    def get_parents(mother: Parent, father: Parent) -> dict[Parent, Parent]:
        return {'mother': mother, 'father': father}
