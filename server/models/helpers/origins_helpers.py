from typing import Optional
from models.helpers.date_helpers import convert_month_year
from models.origins import Parent


def get_parent(name: Optional[str], origin: Optional[str]) -> Optional[Parent]:
    if name is not None:
        return Parent(name, origin)


def get_nz_resident(in_nz_length: Optional[int], lang: str) -> Optional[str]:
    if in_nz_length is not None:
        return convert_month_year(in_nz_length, lang)
    return None
