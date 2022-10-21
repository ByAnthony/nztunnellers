from dataclasses import dataclass
from typing import Optional


@dataclass
class Parent:
    name: Optional[str]
    origin_country: Optional[str]
