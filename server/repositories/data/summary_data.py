# -*- coding: utf-8 -*-
from ...models.roll import Name
from ...models.summary import Summary
from ...models.helpers.date_helpers import (
    format_date_to_year,
)


def summary(forename: str, surname: str, birth_date: str, death_date: str) -> Summary:
    return Summary(
        Name(
            forename,
            surname,
        ),
        format_date_to_year(birth_date),
        format_date_to_year(death_date),
    )
