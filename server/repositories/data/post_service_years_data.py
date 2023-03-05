# -*- coding: utf-8 -*-
from ...models.helpers.date_helpers import get_death_date
from ...models.helpers.military_years_helpers import (
    get_cemetery,
    get_death_circumstances,
    get_death_place,
)
from ...models.helpers.post_service_years_helpers import get_death
from ...models.helpers.translator_helpers import translate_town
from ...models.post_service_years import PostServiceYears
from ...models.tunneller import Tunneller


def post_service_years(tunneller_result: Tunneller, lang: str) -> PostServiceYears:
    return PostServiceYears(
        get_death(
            tunneller_result["death_type"],
            get_death_date(
                tunneller_result["death_year"],
                tunneller_result["death_date"],
                lang,
            ),
            get_death_place(
                tunneller_result["death_location"],
                translate_town(tunneller_result["death_town"], lang),
                tunneller_result["death_country"],
            ),
            get_death_circumstances(
                tunneller_result["death_cause"],
                tunneller_result["death_circumstances"],
            ),
            get_cemetery(
                tunneller_result["cemetery"],
                tunneller_result["cemetery_town"],
                tunneller_result["cemetery_country"],
                tunneller_result["grave"],
            ),
        ),
    )
