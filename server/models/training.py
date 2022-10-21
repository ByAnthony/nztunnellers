from dataclasses import dataclass
from datetime import date


@dataclass
class Training:
    start: str
    location: str
    location_type: str
