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


@app.route("/nz-tunnellers-api/")
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = 'SELECT id, surname, forename, serial, birth_country_fk, birth_country.country_en AS birth_country_en, mother_name, mother_origin_fk, mother_origin.country_en AS mother_origin_en, father_name, father_origin_fk, father_origin.country_en AS father_origin_en, marital_status.marital_status_en, religion.religion_en FROM tunneller t JOIN country birth_country ON t.birth_country_fk=birth_country.country_id JOIN country mother_origin ON t.mother_origin_fk=mother_origin.country_id JOIN country father_origin ON t.father_origin_fk=father_origin.country_id LEFT JOIN marital_status ON t.marital_status_fk=marital_status.marital_status_id LEFT JOIN religion ON t.religion_fk=religion.religion_id'

    cursor.execute(sql)
    result = cursor.fetchall()
    tunnellers = []
    content = {}
    for data in result:
        content = {
            'id': data['id'],
            'forename': data['forename'],
            'surname': data['surname'],
            'serial': data['serial'],
            'birth_country': data['birth_country_en'],
            'parents': {
                'mother_name': data['mother_name'],
                'mother_origin': data['mother_origin_en'],
                'father_name': data['father_name'],
                'father_origin': data['father_origin_en']
            },
            'pre-war': {
                'religion': data['religion_en'],
                'marital_status': data['marital_status_en']
            }
        }
        tunnellers.append(content)
        content = {}
    return jsonify(tunnellers)


if __name__ == '__main__':
    app.run(debug=True)
