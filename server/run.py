from flask import Flask, jsonify
from flask_mysqldb import MySQL
import repositories.tunnellers_repository as tunnellers_repository
import repositories.tunneller_repository as tunneller_repository
from mapper.mapper_tunnellers import map_tunnellers
from mapper.mapper_tunneller import map_tunneller


app = Flask(__name__)


app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_PORT"] = 8889
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nztunnellers_v2"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


@app.route("/tunnellers/", methods=["GET"])
def tunnellers():
    tunnellers = tunnellers_repository.select_all(mysql)
    return jsonify(map_tunnellers(tunnellers))


@app.route("/tunnellers/<id>", methods=["GET"])
def show(id):
    tunneller = tunneller_repository.show(id, mysql)
    return jsonify(map_tunneller(tunneller))


if __name__ == '__main__':
    app.run(debug=True)
