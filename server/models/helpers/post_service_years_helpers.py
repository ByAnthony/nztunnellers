# -*- coding: utf-8 -*-
from typing import Optional

from ..date import Date
from ..death import Cemetery, Death, DeathCause, DeathPlace


def get_death_war_injury(
    death_type: Optional[int],
    date: Optional[Date],
    place: Optional[DeathPlace],
    cause: Optional[DeathCause],
    cemetery: Optional[Cemetery],
) -> Optional[Death]:
    if death_type == 2:
        return Death(date, place, cause, cemetery)
    return None


def get_death(
    date: Optional[Date],
    place: Optional[DeathPlace],
    cause: Optional[DeathCause],
    cemetery: Optional[Cemetery],
) -> Optional[Death]:
    if date is not None:
        return Death(date, place, cause, cemetery)
    return None
