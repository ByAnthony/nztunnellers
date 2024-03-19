# -*- coding: utf-8 -*-
from typing import Optional
from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    format_date_to_year,
)
from ...models.origins import BirthDetails, Origins, Parents


def origins(
    birth_date: str,
    birth_country: str,
    parents: Parents,
    nz_resident: Optional[str],
    lang: str,
) -> Origins:
    return Origins(
        BirthDetails(
            format_birth_and_death_date(
                format_date_to_year(birth_date),
                birth_date,
                lang,
            ),
            birth_country,
        ),
        parents,
        nz_resident,
    )
