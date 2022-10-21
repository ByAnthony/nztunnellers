from dataclasses import dataclass
from .name import Name


@dataclass
class Roll():
    id: int
    serial: str
    name: Name
