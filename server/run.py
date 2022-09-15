from flask import Flask, jsonify
from flask_mysqldb import MySQL
import repositories.roll_repository as tunnellers_repository
import repositories.tunneller_repository as tunneller_repository
from mapper.roll_mapper import map_roll
from mapper.tunneller_mapper import map_tunneller


app = Flask(__name__)


app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_PORT"] = 8889
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nztunnellers_v2"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


@app.route("/roll/", methods=["GET"])
def roll():
    tunnellers = tunnellers_repository.select_all(mysql)
    return jsonify(map_roll(tunnellers))


@app.route("/roll/<id>", methods=["GET"])
def tunneller(id):
    tunneller, nz_archives, london_gazette = tunneller_repository.show(
        id, mysql)
    return jsonify(map_tunneller(tunneller, nz_archives, london_gazette))


if __name__ == '__main__':
    app.run()
