# -*- coding: utf-8 -*-
# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL, MySQLdb  # type: ignore
from typing import Any, Optional, Union


def run_sql(
    sql: str, mysql: MySQL, values: Union[Optional[list[int]], Optional[list[str]]]
) -> tuple[Any]:
    conn = None
    results: Union[tuple[int], tuple[str]]
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        cursor.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
