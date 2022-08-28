from flask import Flask, jsonify
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_PORT"] = 8889
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nztunnellers_v2"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(
        "SELECT id, surname, forename, serial, marital_status.marital_status_en FROM tunneller LEFT JOIN marital_status ON tunneller.marital_status_fk=marital_status.marital_status_id")
    rv = cur.fetchall()
    tunnellers = []
    content = {}
    for result in rv:
        content = {'id': result['id'], 'forename': result['forename'],
                   'surname': result['surname'], 'serial': result['serial'], 'marital_status': result['marital_status_en']}
        tunnellers.append(content)
        content = {}
    return jsonify(tunnellers)


if __name__ == '__main__':
    app.run(debug=True)
