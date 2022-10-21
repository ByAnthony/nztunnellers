from dataclasses import dataclass
from typing import Optional


@dataclass
class Medal:
    name: Optional[str]
    citation: Optional[str]
    country: Optional[str]
