from .date.date_mapper import assert_non_nullish_date_and_format
from .month_year.month_year_mapper import convert_month_year
from .parent.parent_mapper import map_parent
from .birth.birth_mapper import map_birth
from .army_experience.army_experience_mapper import map_army_experience
from .medals.medals_mapper import map_medals
from .nz_archives.nz_archives_mapper import map_nz_archives
from .london_gazette.london_gazette_mapper import map_london_gazette
from .image_source_book_authors.image_source_book_authors_mapper import map_authors


def map_tunneller(tunneller, army_experience, medals, nz_archives, london_gazette, image_source_book_authors, lang):
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
                'mother': map_parent(data['mother_name'], data['mother_origin']),
                'father': map_parent(data['father_name'], data['father_origin'])
            },
            'preWar': {
                'birth': map_birth(data['birth_date'], data['birth_year'], data['birth_country']),
                'migrateToNewZealand': {
                    'newZealandResident': convert_month_year(data['nz_resident_in_month'], lang)
                },
                'civilLife': {
                    'maritalStatus': {
                        'status': data['marital_status'],
                        'wife': data['wife_name']
                    },
                    'religion': data['religion'],
                    'residence': data['town_name'],
                    'occupation': {
                        'name': data['occupation'],
                        'last_employer': data['last_employer_name']
                    }
                },
                'armyExperience': map_army_experience(army_experience, lang)
            },
            'militaryLife': {
                'serial': data['serial'],
                'rank': data['rank'],
                'enlistment': {
                    'date': assert_non_nullish_date_and_format(data['enlistment_date']),
                    'militaryDistrict': data['military_district_name'],
                    'postedToDate': assert_non_nullish_date_and_format(data['posted_date']),
                    'postedFrom': data['posted_from_corps']
                },
                'embarkationUnit': {
                    'embarkationUnit': data['embarkation_unit'],
                    'section': data['section'],
                    'attachedCorps': data['attached_corps'],
                    'training': {
                        'start': assert_non_nullish_date_and_format(data['training_start']),
                        'location': data['training_location'],
                        'locationType': data['training_location_type']
                    },
                    'transportUnitedKindgom': {
                        'id': data['transport_uk_ref'],
                        'vessel': data['transport_uk_vessel'],
                        'departure': assert_non_nullish_date_and_format(data['transport_uk_start']),
                        'from': data['transport_uk_origin'],
                        'arrival': assert_non_nullish_date_and_format(data['transport_uk_end']),
                        'to': data['transport_uk_destination'],
                    }
                },
                'medals': map_medals(medals)
            },
            'sources': {
                'newZealandArchives': map_nz_archives(nz_archives),
                'awmmCenotaph': '{}{}'.format('https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/', data['awmm_cenotaph']),
                'nominalRoll': {
                    'volume': data['nominal_roll_volume'],
                    'roll': data['nominal_roll_number'],
                    'page': data['nominal_roll_page']
                },
                'londonGazette': map_london_gazette(london_gazette)
            },
            'image': {'file': data['image'], 'source': {
                'aucklandLibraries': '{}{}{}'.format('https://digitalnz.org/records?text=', data['image_source_auckland_libraries'], '&tab=Images#'),
                'archives': {'location': data['archives_name'], 'reference': data['archives_ref']},
                'family': data['family_name'],
                'newspaper': {'name': data['newspaper_name'], 'date': assert_non_nullish_date_and_format(data['newspaper_date'])},
                'book': {'authors': map_authors(image_source_book_authors), 'title': data['book_title'], 'town': data['book_town'], 'publisher': data['book_publisher'], 'year': data['book_year'], 'page': data['book_page']}
            }}
        }
    return profile
