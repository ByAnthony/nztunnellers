from mapper.date_mapper import format_date, assert_non_nullish_date
from mapper.parent_mapper import map_parent
from mapper.birth_mapper import map_birth
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
                'birth': map_birth(data['birth_date'], data['birth_country_en']),
                'migrate_to_nz': {
                    'nz_resident': data['nz_resident_in_month']
                },
                'civil_life': {
                    'marital_status': {
                        'status': data['marital_status_en'],
                        'wife': data['wife_name']
                    },
                    'religion': data['religion_en'],
                    'occupation': {
                        'name': data['occupation_en']
                    }
                }
            },
            'military_life': {
                'serial': data['serial'],
                'rank': data['rank_en'],
                'enlistment': {
                    'date': assert_non_nullish_date(data['enlistment_date']),
                    'military_district': data['military_district_name'],
                    'posted_to_tunnellers': assert_non_nullish_date(data['posted_date']),
                    'posted_from': data['posted_from_corps_en']
                },
                'embarkation_unit': {
                    'embarkation_unit': data['embarkation_unit_en'],
                    'section': data['section_en'],
                    'attached_corps': data['attached_corps_en'],
                    'training': {
                        'start': format_date(data['training_start']),
                        'location': data['training_location'],
                        'location_type': data['training_location_type_en']
                    },
                    'transport_uk': {
                        'id': data['transport_uk_ref'],
                        'vessel': data['transport_uk_vessel'],
                        'departure': format_date(data['transport_uk_start']),
                        'from': data['transport_uk_origin'],
                        'arrival': format_date(data['transport_uk_end']),
                        'to': data['transport_uk_destination'],
                    }
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
