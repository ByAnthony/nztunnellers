# -*- coding: utf-8 -*-
from dataclasses import asdict
from typing import Any


from ..repositories.queries.roll_query import roll_query

from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.roll import Name, Roll


def select_all(mysql: MySQL) -> dict[list[dict[Roll, Any]], Any]:

    sql: str = roll_query()
    results: list[Roll] = run_sql(sql, mysql, None)

    alphabet: dict[list[dict[Roll, Any]], Any] = dict()

    for row in results:
        character = row["surname"][:1].upper()
        tunneller = asdict(
            Roll(
                row["id"],
                Name(row["forename"], row["surname"]),
                row["birth_year"],
                row["death_year"],
            )
        )
        if character in alphabet:
            alphabet[character].append(tunneller)
        else:
            alphabet[character] = list()
            alphabet[character].append(tunneller)

    return alphabet
