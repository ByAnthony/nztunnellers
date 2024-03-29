# -*- coding: utf-8 -*-
# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL  # type: ignore

from ..repositories.queries.roll_query import roll_query

from ..db.models.RollData import RollData
from ..db.run_sql import run_sql
from ..models.roll import Name, Roll

from ..models.helpers.date_helpers import (
    format_date_to_year,
)


def select_all(mysql: MySQL) -> dict[str, list[Roll]]:

    sql: str = roll_query()
    results: tuple[RollData, ...] = run_sql(sql, mysql, None)

    alphabet: dict[str, list[Roll]] = dict()

    for row in results:
        character = row["surname"][:1].upper()
        tunneller = Roll(
            row["id"],
            Name(row["forename"], row["surname"]),
            format_date_to_year(row["birth_date"]),
            format_date_to_year(row["death_date"]),
        )
        if character in alphabet:
            alphabet[character].append(tunneller)
        else:
            alphabet[character] = list()
            alphabet[character].append(tunneller)

    return alphabet
