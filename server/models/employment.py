from dataclasses import dataclass
from typing import Optional


class Employment:
    occupation: str
    employer: Optional[str]

    def get_employment(occupation: str, employer: Optional[str]) -> dict[str, Optional[str]]:
        return {'occupation': occupation, 'employer': employer}
