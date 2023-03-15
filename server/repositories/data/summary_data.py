# -*- coding: utf-8 -*-
from ...models.roll import Name
from ...models.tunneller import Tunneller
from ...models.summary import Summary


def summary(tunneller_result: Tunneller) -> Summary:
    return Summary(
        Name(
            tunneller_result["forename"],
            tunneller_result["surname"],
        ),
        tunneller_result["birth_year"],
        tunneller_result["death_year"],
    )
