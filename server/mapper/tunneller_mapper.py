from mapper.date.date_mapper import assert_non_nullish_date_and_format
from mapper.parent.parent_mapper import map_parent
from mapper.birth.birth_mapper import map_birth
from mapper.nz_archives.nz_archives_mapper import map_nz_archives
from mapper.london_gazette.london_gazette_mapper import map_london_gazette


def map_tunneller(tunneller, london_gazette):
    profile = None
    for data in tunneller:
        profile = {
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
                    'date': assert_non_nullish_date_and_format(data['enlistment_date']),
                    'military_district': data['military_district_name'],
                    'posted_to_date': assert_non_nullish_date_and_format(data['posted_date']),
                    'posted_from': data['posted_from_corps_en']
                },
                'embarkation_unit': {
                    'embarkation_unit': data['embarkation_unit_en'],
                    'section': data['section_en'],
                    'attached_corps': data['attached_corps_en'],
                    'training': {
                        'start': assert_non_nullish_date_and_format(data['training_start']),
                        'location': data['training_location'],
                        'location_type': data['training_location_type_en']
                    },
                    'transport_uk': {
                        'id': data['transport_uk_ref'],
                        'vessel': data['transport_uk_vessel'],
                        'departure': assert_non_nullish_date_and_format(data['transport_uk_start']),
                        'from': data['transport_uk_origin'],
                        'arrival': assert_non_nullish_date_and_format(data['transport_uk_end']),
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
                'london_gazette': map_london_gazette(london_gazette)
            }
        }
    return profile
