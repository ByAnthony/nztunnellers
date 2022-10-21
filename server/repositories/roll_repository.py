from db.run_sql import run_sql
from models.roll import Roll
from models.name import Name


def select_all(mysql):

    roll = []
    sql = f'''
        SELECT id, surname, forename, serial
        FROM tunneller t
        ORDER BY surname, forename
    '''
    results = run_sql(sql, mysql)

    for row in results:
        tunneller = Roll(row['id'], row['serial'], Name(
            row['forename'], row['surname']))
        roll.append(tunneller)
    return roll
