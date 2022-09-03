import datetime
from mapper.parent_mapper import map_parent
from mapper.date_mapper import map_birth, format_year, format_date
from mapper.nz_archives_mapper import map_nz_archives


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
                'rank': data['rank_en'],
                'embarkation_unit': {
                    'embarkation_unit': data['embarkation_unit_en'],
                    'training': {
                        'training_start': format_date(data['training_start']),
                        'training_location': data['training_location'],
                        'training_location_type': data['training_location_type_en']
                    },
                },
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
