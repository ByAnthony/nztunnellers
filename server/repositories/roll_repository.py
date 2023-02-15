# -*- coding: utf-8 -*-
from dataclasses import asdict
from typing import Any


from ..models.helpers.date_helpers import format_date_to_birth_year
from ..models.helpers.name_helpers import set_surname_to_uppercase
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
                Name(row["forename"], set_surname_to_uppercase(row["surname"])),
                format_date_to_birth_year(
                    row["birth_year"],
                    row["birth_date"],
                ),
                format_date_to_birth_year(
                    row["death_year"],
                    row["death_date"],
                ),
            )
        )
        print(row["birth_year"])
        if character in alphabet:
            alphabet[character].append(tunneller)
        else:
            alphabet[character] = list()
            alphabet[character].append(tunneller)

    return alphabet
