# -*- coding: utf-8 -*-
from ...db.models.TunnellerData import TunnellerData
from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    format_date_to_year,
)
from ...models.helpers.origins_helpers import get_nz_resident, get_parent
from ...models.origins import BirthDetails, Origins, Parents


def origins(tunneller: TunnellerData, lang: str) -> Origins:
    return Origins(
        BirthDetails(
            format_birth_and_death_date(
                format_date_to_year(tunneller["birth_date"]),
                tunneller["birth_date"],
                lang,
            ),
            tunneller["birth_country"],
        ),
        Parents(
            get_parent(
                tunneller["mother_name"],
                tunneller["mother_origin"],
            ),
            get_parent(
                tunneller["father_name"],
                tunneller["father_origin"],
            ),
        ),
        get_nz_resident(
            tunneller["nz_resident_in_month"],
            tunneller["enlistment_date"],
        ),
    )
