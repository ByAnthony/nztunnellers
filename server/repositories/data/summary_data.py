# -*- coding: utf-8 -*-
from ...models.helpers.date_helpers import format_date_to_birth_year
from ...models.roll import Name
from ...models.tunneller import Tunneller
from ...models.summary import Summary


def summary(tunneller_result: Tunneller) -> Summary:
    return Summary(
        Name(
            tunneller_result["forename"],
            tunneller_result["surname"],
        ),
        format_date_to_birth_year(
            tunneller_result["birth_year"],
            tunneller_result["birth_date"],
        ),
        format_date_to_birth_year(
            tunneller_result["death_year"],
            tunneller_result["death_date"],
        ),
    )
