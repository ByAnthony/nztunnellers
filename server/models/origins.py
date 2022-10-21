from dataclasses import dataclass
from typing import Optional
from .parents import Parents
from .birth_details import BirthDetails


@dataclass
class Origins:
    birth: BirthDetails
    parents: Parents
    in_nz_length: Optional[str]
