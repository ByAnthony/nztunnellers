from dataclasses import dataclass
from typing import Optional


@dataclass
class BirthDetails:
    year: Optional[str]
    date: Optional[str]
    country: Optional[str]
