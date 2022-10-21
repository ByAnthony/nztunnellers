from dataclasses import dataclass
from typing import Optional


@dataclass
class Transport:
    transport_reference: str
    vessel: str
    departure_date: str
    departure_port: Optional[str]
    arrival_date: Optional[str]
    arrival_port: Optional[str]
