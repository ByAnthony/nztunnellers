from flask_mysqldb import MySQLdb


def run_sql(sql, mysql, values=None):
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
