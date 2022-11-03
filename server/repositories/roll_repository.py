# -*- coding: utf-8 -*-
from dataclasses import asdict
from typing import Any

from db.run_sql import run_sql
from flask_mysqldb import MySQL
from models.roll import Name, Roll


def select_all(mysql: MySQL) -> list[dict[str, Any]]:

    sql: str = f"""
        SELECT t.id, t.surname, t.forename, t.serial
        FROM tunneller t
        ORDER BY t.surname, t.forename
    """
    results: list[Roll] = run_sql(sql, mysql, None)

    tunnellers: list[dict[str, Any]] = [
        asdict(Roll(row["id"], row["serial"], Name(row["forename"], row["surname"])))
        for row in results
    ]
    return tunnellers
