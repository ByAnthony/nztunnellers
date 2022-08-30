from flask import Flask, jsonify
from flask_mysqldb import MySQL, MySQLdb
from sql.query import sql
from mapper.mapper_roll import map_roll


app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_PORT"] = 8889
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nztunnellers_v2"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/roll/")
def roll():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    sql_data = cursor.fetchall()

    return jsonify(map_roll(sql_data))


if __name__ == '__main__':
    app.run(debug=True)
