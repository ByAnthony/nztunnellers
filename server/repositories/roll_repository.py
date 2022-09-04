from db.run_sql import run_sql


def select_all(mysql):
    sql = f'''
        SELECT id, surname, forename, serial
        FROM tunneller t
        ORDER BY surname, forename
    '''
    results = run_sql(sql, mysql)
    return results
