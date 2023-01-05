# -*- coding: utf-8 -*-
from dataclasses import asdict
from typing import Any

from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.roll import Name, Roll


def select_all(mysql: MySQL) -> dict[list[dict[Roll, Any]], Any]:

    sql: str = "SELECT t.id, t.surname, t.forename, t.serial FROM tunneller t ORDER BY t.surname, t.forename"
    results: list[Roll] = run_sql(sql, mysql, None)

    alphabet: dict[list[dict[Roll, Any]], Any] = dict()
    for row in results:
        character = row["surname"][:1].upper()
        if character in alphabet:
            alphabet[character].append(
                asdict(
                    Roll(
                        row["id"], row["serial"], Name(row["forename"], row["surname"])
                    )
                )
            )
        else:
            alphabet[character] = list()
            alphabet[character].append(
                asdict(
                    Roll(
                        row["id"], row["serial"], Name(row["forename"], row["surname"])
                    )
                )
            )

    return alphabet
