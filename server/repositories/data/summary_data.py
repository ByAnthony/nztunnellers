# -*- coding: utf-8 -*-
from ...models.roll import Name
from ...models.tunneller import Tunneller
from ...models.summary import Summary


def summary(tunneller: Tunneller) -> Summary:
    return Summary(
        Name(
            tunneller["forename"],
            tunneller["surname"],
        ),
        tunneller["birth_year"],
        tunneller["death_year"],
    )
