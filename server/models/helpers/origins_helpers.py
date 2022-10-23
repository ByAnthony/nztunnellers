from typing import Optional
from models.helpers.date_helpers import convert_month_year


def get_parent(name: Optional[str], origin: Optional[str]) -> Optional[dict[Optional[str], Optional[str]]]:
    if name and origin is not None:
        return {'name': name, 'origin': origin}
    return None


def get_nz_resident(in_nz_in_month: Optional[int], lang: str) -> Optional[str]:
    if in_nz_in_month is not None:
        return convert_month_year(in_nz_in_month, lang)
    return None
