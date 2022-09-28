from .converter.month_year_converter import convert_month_year
from .formatter.auckland_libraries_link_formatter import format_auckland_libraries_link
from .formatter.birth_formatter import format_birth
from .formatter.date_formatter import assert_non_nullish_date_and_format
from .formatter.nominal_roll_formatter import format_nominal_roll
from .formatter.parent_formatter import format_parent
from .mapper.army_experience_mapper import map_army_experience
from .mapper.image_source_book_authors_mapper import map_authors
from .mapper.london_gazette_mapper import map_london_gazette
from .mapper.medals_mapper import map_medals
from .mapper.nz_archives_mapper import map_nz_archives
from .translator.family_translator import translate_family
from .translator.superscript_translator import translate_superscript
from .translator.transport_ref_translator import translate_transport_ref


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
                'mother': format_parent(data['mother_name'], data['mother_origin']),
                'father': format_parent(data['father_name'], data['father_origin'])
            },
            'preWar': {
                'birth': format_birth(data['birth_date'], data['birth_year'], data['birth_country']),
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
                    'embarkationUnit': translate_superscript(data['embarkation_unit'], lang),
                    'section': translate_superscript(data['section'], lang),
                    'attachedCorps': data['attached_corps'],
                    'training': {
                        'start': assert_non_nullish_date_and_format(data['training_start']),
                        'location': data['training_location'],
                        'locationType': data['training_location_type']
                    },
                    'transportUnitedKindgom': {
                        'id': translate_transport_ref(data['transport_uk_ref'], lang),
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
                'nominalRoll': format_nominal_roll(data['nominal_roll_volume'], data['nominal_roll_number'], data['nominal_roll_page'], lang),
                'londonGazette': map_london_gazette(london_gazette)
            },
            'image': {'file': data['image'], 'source': {
                'aucklandLibraries': format_auckland_libraries_link(data['image_source_auckland_libraries']),
                'archives': {'location': data['archives_name'], 'reference': data['archives_ref']},
                'family': translate_family(data['family_name'], lang),
                'newspaper': {'name': data['newspaper_name'], 'date': assert_non_nullish_date_and_format(data['newspaper_date'])},
                'book': {'authors': map_authors(image_source_book_authors), 'title': data['book_title'], 'town': data['book_town'], 'publisher': data['book_publisher'], 'year': data['book_year'], 'page': data['book_page']}
            }}
        }
    return profile
