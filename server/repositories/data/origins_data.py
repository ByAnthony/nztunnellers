# -*- coding: utf-8 -*-
from ...models.helpers.date_helpers import get_birth_date
from ...models.helpers.origins_helpers import get_nz_resident, get_parent
from ...models.origins import BirthDetails, Origins, Parents
from ...models.tunneller import Tunneller


def origins(tunneller_result: Tunneller, lang: str) -> Origins:
    return Origins(
        BirthDetails(
            get_birth_date(
                tunneller_result["birth_year"], tunneller_result["birth_date"], lang
            ),
            tunneller_result["birth_country"],
        ),
        Parents(
            get_parent(
                tunneller_result["mother_name"],
                tunneller_result["mother_origin"],
            ),
            get_parent(
                tunneller_result["father_name"],
                tunneller_result["father_origin"],
            ),
        ),
        get_nz_resident(
            tunneller_result["nz_resident_in_month"],
            tunneller_result["enlistment_date"],
        ),
    )
