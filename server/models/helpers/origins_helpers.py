# -*- coding: utf-8 -*-
from typing import Optional

from .date_helpers import convert_immigration_year
from ..origins import Parent


def get_parent(name: Optional[str], origin: Optional[str]) -> Optional[Parent]:
    if name is None:
        return None
    return Parent(name, origin)


def get_nz_resident(
    in_nz_length: Optional[str], enlistment_date: Optional[str]
) -> Optional[str]:
    if in_nz_length is None:
        return None
    return convert_immigration_year(in_nz_length, enlistment_date)
