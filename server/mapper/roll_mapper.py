def map_roll(response):
    tunnellers = []
    for data in response:
        content = {
            'id': data['id'],
            'forename': data['forename'],
            'surname': data['surname'],
            'serial': data['serial']
        }
        tunnellers.append(content)
    return tunnellers
