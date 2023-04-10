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
    age_at_death: Optional[int],
) -> Optional[DeathAfterService]:
    if death_type == "War injuries":
        return DeathAfterService(date, place, cause, cemetery, age_at_death, True)
    if death_type == "After war":
        return DeathAfterService(date, place, cause, cemetery, age_at_death, False)
    if death_type is None and date is not None:
        return DeathAfterService(date, place, cause, cemetery, age_at_death, None)
    return None
