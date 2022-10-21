from db.run_sql import run_sql
from models.roll import Roll
from models.name import Name


def select_all(mysql):

    roll = []
    sql = f'''
        SELECT t.id, t.surname, t.forename, t.serial
        FROM tunneller t
        ORDER BY t.surname, t.forename
    '''
    results = run_sql(sql, mysql)

    for row in results:
        tunneller = Roll(row['id'], row['serial'], Name(
            row['forename'], row['surname']))
        roll.append(tunneller)
    return roll
