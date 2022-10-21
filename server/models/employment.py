from dataclasses import dataclass
from typing import Optional


@dataclass
class Employment:
    occupation: str
    employer: Optional[str]
