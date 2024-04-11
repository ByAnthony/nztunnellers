# -*- coding: utf-8 -*-
# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL, MySQLdb  # type: ignore
from typing import Any, Optional, Union


def run_sql(
    sql: str, mysql: MySQL, values: Union[Optional[list[int]], Optional[list[str]]]
) -> tuple[Any, ...]:
    cursor = None
    results: tuple[Any, ...]
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  # type: ignore
        cursor.execute(sql, values)  # type: ignore
        results = cursor.fetchall()  # type: ignore
        cursor.close()  # type: ignore
    except (Exception) as error:
        results = tuple()
        print(error)
    finally:
        if cursor is not None:
            cursor.close()  # type: ignore
    return results  # type: ignore
