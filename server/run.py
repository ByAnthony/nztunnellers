from flask import Flask, jsonify
from flask_mysqldb import MySQL, MySQLdb
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


def run_sql(sql, values=None):
    conn = None
    results = []
    try:
        conn = config_sql()
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


@app.route("/tunnellers/")
def tunnellers():
    sql = f'''SELECT id, surname, forename, serial
            FROM tunneller t
            ORDER BY surname, forename
        '''
    results = run_sql(sql)
    return jsonify(map_tunnellers(results))


@app.route("/tunnellers/<id>")
def show(id):
    sql = f'''
        SELECT id, surname, forename, serial, birth_country_fk, birth_country.country_en AS birth_country_en, mother_name, mother_origin_fk, mother_origin.country_en AS mother_origin_en, father_name, father_origin_fk, father_origin.country_en AS father_origin_en, marital_status.marital_status_en, religion.religion_en

        FROM tunneller t

        LEFT JOIN country birth_country ON t.birth_country_fk=birth_country.country_id
        LEFT JOIN country mother_origin ON t.mother_origin_fk=mother_origin.country_id
        LEFT JOIN country father_origin ON t.father_origin_fk=father_origin.country_id
        LEFT JOIN marital_status ON t.marital_status_fk=marital_status.marital_status_id
        LEFT JOIN religion ON t.religion_fk=religion.religion_id

        WHERE id=%s

        ORDER BY surname, forename
    '''
    values = [id]
    result = run_sql(sql, values)
    return jsonify(map_tunneller(result))


if __name__ == '__main__':
    app.run(debug=True)
