from flask_mysqldb import MySQL
from dataclasses import asdict
from db.run_sql import run_sql
from models.roll import Roll, Name


def select_all(mysql: MySQL) -> list[Roll]:

    sql: str = f'''
        SELECT t.id, t.surname, t.forename, t.serial
        FROM tunneller t
        ORDER BY t.surname, t.forename
    '''
    results: list[Roll] = run_sql(sql, mysql, None)

    tunnellers = [asdict(Roll(row['id'], row['serial'], Name(
        row['forename'], row['surname']))) for row in results]
    return tunnellers
