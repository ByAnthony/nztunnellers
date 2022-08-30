def map_roll(sql_data):
    roll = []
    for data in sql_data:
        content = {
            'id': data['id'],
            'forename': data['forename'],
            'surname': data['surname'],
            'serial': data['serial']
        }
        roll.append(content)
    return roll
