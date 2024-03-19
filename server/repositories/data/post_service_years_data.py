# -*- coding: utf-8 -*-
from typing import Optional

from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    format_date_to_year,
)
from ...models.death import Cemetery, DeathCause, DeathPlace
from ...models.helpers.post_service_years_helpers import get_death
from ...models.post_service_years import PostServiceYears


def post_service_years(
    death_type: str,
    death_date: str,
    death_place: Optional[DeathPlace],
    death_circumstances: Optional[DeathCause],
    cemetery: Optional[Cemetery],
    age_at_death: Optional[int],
    lang: str,
) -> PostServiceYears:
    return PostServiceYears(
        get_death(
            death_type,
            format_birth_and_death_date(
                format_date_to_year(death_date),
                death_date,
                lang,
            ),
            death_place,
            death_circumstances,
            cemetery,
            age_at_death,
        ),
    )
