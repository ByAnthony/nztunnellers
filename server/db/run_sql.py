from typing import Optional
from flask_mysqldb import MySQL, MySQLdb


def run_sql(sql: str, mysql: MySQL, values: Optional[list[int]]):
    conn = None
    results = []
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
