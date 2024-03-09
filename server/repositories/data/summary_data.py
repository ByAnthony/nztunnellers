# -*- coding: utf-8 -*-
from ...db.models.TunnellerData import TunnellerData
from ...models.roll import Name
from ...models.summary import Summary
from ...models.helpers.date_helpers import (
    format_date_to_year,
)


def summary(tunneller: TunnellerData) -> Summary:
    return Summary(
        Name(
            tunneller["forename"],
            tunneller["surname"],
        ),
        format_date_to_year(tunneller["birth_date"]),
        format_date_to_year(tunneller["death_date"]),
    )
