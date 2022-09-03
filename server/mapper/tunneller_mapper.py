def map_tunneller(response):
    tunneller = None
    for data in response:
        tunneller = {
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
    return tunneller
