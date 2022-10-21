from typing import Optional
from models.helpers.formatter_date import convert_month_year


def get_nz_resident(in_nz_in_month: Optional[int], lang: str) -> Optional[str]:
    if in_nz_in_month is not None:
        return convert_month_year(in_nz_in_month, lang)
    return None
