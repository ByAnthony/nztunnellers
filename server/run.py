from flask import Flask, request
from flask_mysqldb import MySQL
# from mapper.tunneller_mapper import map_tunneller

import os
import json
import repositories.roll_repository as tunnellers_repository
import repositories.tunneller_repository as tunneller_repository


app = Flask(__name__)


if os.environ.get('DEV') == 'true':
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
else:
    app.config['MYSQL_USER'] = ''
    app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'nztunnellers_v2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route('/roll/', methods=['GET'])
def roll():
    tunnellers = tunnellers_repository.select_all(mysql)
    roll = json.dumps(
        [tunneller.__dict__ for tunneller in tunnellers], indent=4)
    return roll


@app.route('/roll/<id>', methods=['GET'])
def tunneller(id):
    lang = request.args.get('lang', 'en')
    if lang not in ['en', 'fr']:
        return 'Language not supported', 400
    # tunneller, army_experience, medals, nz_archives, london_gazette, image_source_book_authors = tunneller_repository.show(
    #     id, lang, mysql)
    # return jsonify(map_tunneller(tunneller, army_experience, medals, nz_archives, london_gazette, image_source_book_authors, lang))
    tunneller = tunneller_repository.show(id, lang, mysql)
    profile = json.dumps(tunneller.__dict__, indent=4)
    return profile


if __name__ == '__main__':
    app.run(debug=True)
