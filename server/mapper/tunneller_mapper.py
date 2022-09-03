import datetime


def map_tunneller(response):
    tunneller = None
    for data in response:
        tunneller = {
            'id': data['id'],
            'name': {
                'forename': data['forename'],
                'surname': data['surname'],
                'aka': data['aka']
            },
            'parents': {
                'mother': map_parent(data['mother_name'], data['mother_origin_en']),
                'father': map_parent(data['father_name'], data['father_origin_en'])
            },
            'pre_war': {
                'birth': map_birth(format_year(data['birth_date']), data['birth_country_en']),
                'religion': data['religion_en'],
                'marital_status': data['marital_status_en']
            },
            'military_life': {
                'serial': data['serial'],
                'rank': data['rank_en']
            },
            'sources': {
                'nz_archives': map_nz_archives(data['nz_archives_ref_1'], data['nz_archives_url_1'], data['nz_archives_ref_2'], data['nz_archives_url_2']),
                'awmm_cenotaph': data['awmm_cenotaph'],
                'nominal_roll': {
                    'volume': data['nominal_roll_volume'],
                    'roll': data['nominal_roll_number'],
                    'page': data['nominal_roll_page']
                },
            }
        }
    return tunneller


def map_parent(name, origin):
    return {'name': name, 'origin': origin}


def map_birth(year, country):
    return {'year': year, 'country': country}


def map_nz_archives(ref_1, url_1, ref_2, url_2):
    if (ref_2 is not None and url_2 is not None):
        return [
            {'ref': ref_1, 'url': url_1},
            {'ref': ref_2, 'url': url_2}
        ]
    return [
        {'ref': ref_1, 'url': url_1}
    ]


def format_year(date):
    return date.strftime('%Y')
