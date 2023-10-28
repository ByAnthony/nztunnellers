# -*- coding: utf-8 -*-
from ..repositories.queries.roll_query import roll_query

from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.roll import Name, Roll


def select_all(mysql: MySQL) -> dict[str, list[Roll]]:

    sql: str = roll_query()
    results: list[Roll] = run_sql(sql, mysql, None)

    alphabet: dict[str, list[Roll]] = dict()

    for row in results:
        character = row["surname"][:1].upper()
        tunneller = Roll(
            row["id"],
            Name(row["forename"], row["surname"]),
            row["birth_year"],
            row["death_year"],
        )
        if character in alphabet:
            alphabet[character].append(tunneller)
        else:
            alphabet[character] = list()
            alphabet[character].append(tunneller)

    return alphabet
