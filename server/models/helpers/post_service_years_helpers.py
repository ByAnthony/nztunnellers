# -*- coding: utf-8 -*-
from typing import Optional

from ..post_service_years import DeathAfterService

from ..date import Date
from ..death import Cemetery, DeathCause, DeathPlace


def get_death(
    death_type: Optional[str],
    date: Optional[Date],
    place: Optional[DeathPlace],
    cause: Optional[DeathCause],
    cemetery: Optional[Cemetery],
) -> Optional[DeathAfterService]:
    if death_type == "War injuries":
        return DeathAfterService(date, place, cause, cemetery, True)
    elif death_type == "After war":
        return DeathAfterService(date, place, cause, cemetery, False)
    return None
