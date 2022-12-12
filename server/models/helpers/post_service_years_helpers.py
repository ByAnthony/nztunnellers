# -*- coding: utf-8 -*-
from typing import Optional

from ..date import Date
from ..death import Cemetery, Death, DeathCause, DeathPlace


def get_death(
    death_type: Optional[int],
    date: Optional[Date],
    place: Optional[DeathPlace],
    cause: Optional[DeathCause],
    cemetery: Optional[Cemetery],
) -> Optional[Death]:
    if death_type != 1:
        return Death(date, place, cause, cemetery)
    return None
