# -*- coding: utf-8 -*-
import json
import os

from flask_cors import CORS


from .models.helpers.camelize_helpers import underscore_to_camel
from .repositories import article_repository
from .repositories import roll_repository
from .repositories import tunneller_repository
from flask import Flask, request
from flask_mysqldb import MySQL
from .models.tunneller import JSONEncoder

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r"/": {"origins": ""}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config["CORS_HEADERS"] = "Content-Type"


if os.environ.get("DEV") == "true":
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "root"
else:
    app.config["MYSQL_USER"] = ""
    app.config["MYSQL_PASSWORD"] = ""

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_DB"] = "nztunnellers_v2"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


@app.route("/tunnellers/", methods=["GET"])
def roll():
    tunnellers = roll_repository.select_all(mysql)
    roll = json.dumps(tunnellers, cls=JSONEncoder, indent=4)
    return roll


@app.route("/tunnellers/<id>", methods=["GET"])
def tunneller(id: int):
    lang = request.args.get("lang", "en")
    if lang not in ["en", "fr"]:
        return "Language not supported", 400
    tunneller = tunneller_repository.show(id, lang, mysql)
    profile = json.dumps(tunneller, cls=JSONEncoder, indent=4)
    camelized_profile_for_ts: str = underscore_to_camel(profile)
    return camelized_profile_for_ts


@app.route("/history/<id>", methods=["GET"])
def article(id: str):
    article = article_repository.show(id, mysql)
    data = json.dumps(article, cls=JSONEncoder, indent=4)
    return data


if __name__ == "__main__":
    app.run(debug=True)
