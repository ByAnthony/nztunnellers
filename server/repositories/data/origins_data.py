# -*- coding: utf-8 -*-
from ...models.helpers.date_helpers import format_birth_and_death_date
from ...models.helpers.origins_helpers import get_nz_resident, get_parent
from ...models.origins import BirthDetails, Origins, Parents
from ...models.tunneller import Tunneller


def origins(tunneller: Tunneller, lang: str) -> Origins:
    return Origins(
        BirthDetails(
            format_birth_and_death_date(
                tunneller["birth_year"], tunneller["birth_date"], lang
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
