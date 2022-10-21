from dataclasses import dataclass
from typing import Optional
from .parents import Parents
from .birth_details import BirthDetails
from .helpers.month_year_converter import convert_month_year


@dataclass
class Origins:
    birth: BirthDetails
    parents: Parents
    in_nz_length: Optional[str]

    def get_nz_resident(in_nz_in_month: Optional[str], lang: str) -> Optional[str]:
        if in_nz_in_month is not None:
            return convert_month_year(in_nz_in_month, lang)
        return None
