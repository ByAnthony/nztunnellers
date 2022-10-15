from db.run_sql import run_sql
from models.roll import Roll


def select_all(mysql):

    roll = []
    sql = f'''
        SELECT id, surname, forename, serial
        FROM tunneller t
        ORDER BY surname, forename
    '''
    results = run_sql(sql, mysql)

    for row in results:
        tunneller = Roll(Roll.get_id(row['id']), Roll.get_serial(
            row['serial']), Roll.get_name(row['forename'], row['surname']))
        roll.append(tunneller)
    return roll
