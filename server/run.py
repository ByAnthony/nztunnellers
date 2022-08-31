from flask import Flask, jsonify
from flask_mysqldb import MySQL, MySQLdb
from sql.query_sql import sql
from mapper.mapper_tunnellers import map_tunnellers
from mapper.mapper_tunneller import map_tunneller


app = Flask(__name__)


def config_sql():
    app.config["MYSQL_HOST"] = "127.0.0.1"
    app.config["MYSQL_PORT"] = 8889
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "root"
    app.config["MYSQL_DB"] = "nztunnellers_v2"
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


def run_sql():
    conn = None
    results = []
    try:
        conn = config_sql()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results


@app.route("/tunnellers/")
def tunnellers():
    return jsonify(map_tunnellers(run_sql()))


@app.route("/tunnellers/<id>")
def tunneller(id):
    return jsonify(map_tunneller(id, run_sql()))


if __name__ == '__main__':
    app.run(debug=True)
