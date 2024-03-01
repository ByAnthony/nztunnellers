# -*- coding: utf-8 -*-
from ...models.helpers.date_helpers import (
    format_birth_and_death_date, 
    format_date_to_year,
)
from ...models.helpers.military_years_helpers import (
    get_age,
    get_cemetery,
    get_death_circumstances,
    get_death_place,
)
from ...models.helpers.post_service_years_helpers import get_death
from ...models.helpers.translator_helpers import translate_town
from ...models.post_service_years import PostServiceYears
from ...models.tunneller import Tunneller


def post_service_years(tunneller: Tunneller, lang: str) -> PostServiceYears:
    return PostServiceYears(
        get_death(
            tunneller["death_type"],
            format_birth_and_death_date(
                format_date_to_year(tunneller["death_date"]),
                tunneller["death_date"],
                lang,
            ),
            get_death_place(
                tunneller["death_location"],
                translate_town(tunneller["death_town"], lang),
                tunneller["death_country"],
            ),
            get_death_circumstances(
                tunneller["death_cause"],
                tunneller["death_circumstances"],
            ),
            get_cemetery(
                tunneller["cemetery"],
                tunneller["cemetery_town"],
                tunneller["cemetery_country"],
                tunneller["grave"],
            ),
            get_age(
                format_date_to_year(tunneller["death_date"]),
                tunneller["death_date"],
                format_date_to_year(tunneller["birth_date"]),
                tunneller["birth_date"],
            ),
        ),
    )
