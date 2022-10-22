from db.run_sql import run_sql
from dacite import from_dict
from models.tunneller import Tunneller
from models.helpers.formatter_date import format_date, get_year
from models.helpers.formatter_parent import get_parent
from models.helpers.formatter_nz_resident import get_nz_resident
from models.helpers.mapper_army_experience import map_army_experience
from models.helpers.formatter_transferred_to_tunnellers import get_transferred_to_tunnellers
from models.helpers.formatter_embarkation_unit import get_detachment, get_section
from models.helpers.formatter_training import get_training
from models.helpers.formatter_transport import get_transport_reference
from models.helpers.mapper_medals import map_medals
from .translations.translations import attached_corps_col
from .translations.translations import birth_country_col
from .translations.translations import conflict_col
from .translations.translations import country_col
from .translations.translations import embarkation_unit_col
from .translations.translations import father_origin_col
from .translations.translations import marital_status_col
from .translations.translations import medal_citation_col
from .translations.translations import medal_name_col
from .translations.translations import mother_origin_col
from .translations.translations import occupation_col
from .translations.translations import posted_from_corps_col
from .translations.translations import rank_col
from .translations.translations import religion_col
from .translations.translations import section_col
from .translations.translations import training_location_type_col


def show(id, lang, mysql):

    tunneller = []

    tunneller_sql = f'''
        SELECT t.id, t.forename, t.surname, t.aka, t.serial, t.birth_date, t.birth_year, t.birth_country_fk, {birth_country_col[lang]} AS birth_country, t.mother_name, t.mother_origin_fk, {mother_origin_col[lang]} AS mother_origin, t.father_name, t.father_origin_fk, {father_origin_col[lang]} AS father_origin, nz_resident_in_month, t.marital_status_fk, {marital_status_col[lang]} AS marital_status, t.wife_name, t.occupation_fk, {occupation_col[lang]} AS occupation, t.last_employer_fk, employer.last_employer_name AS employer, t.town_fk, residence.town_name AS residence, t.religion_fk, {religion_col[lang]} AS religion, t.enlistment_date, t.military_district_fk, military_district.military_district_name, t.aka, t.posted_date, t.posted_corps_fk, {posted_from_corps_col[lang]} AS posted_from_corps, t.rank_fk, {rank_col[lang]} AS rank, t.embarkation_unit_fk, {embarkation_unit_col[lang]} AS embarkation_unit, t.section_fk, {section_col[lang]} AS section, t.attached_corps_fk, {attached_corps_col[lang]} AS attached_corps, embarkation_unit.training_fk, training.training_start, training.training_location, {training_location_type_col[lang]} AS training_location_type, embarkation_unit.transport_uk_fk, transport.transport_ref_fk, transport_uk_ref.transport_ref_name AS transport_uk_ref, transport.transport_vessel_fk, transport_uk_vessel.transport_vessel_name AS transport_uk_vessel, transport.transport_start AS transport_uk_start, transport.transport_origin AS transport_uk_origin, transport.transport_end AS transport_uk_end, transport.transport_destination AS transport_uk_destination

        FROM tunneller t

        LEFT JOIN country birth_country ON t.birth_country_fk=birth_country.country_id
        LEFT JOIN country mother_origin ON t.mother_origin_fk=mother_origin.country_id
        LEFT JOIN country father_origin ON t.father_origin_fk=father_origin.country_id
        LEFT JOIN marital_status ON t.marital_status_fk=marital_status.marital_status_id
        LEFT JOIN occupation ON t.occupation_fk=occupation.occupation_id
        LEFT JOIN last_employer employer ON t.last_employer_fk=employer.last_employer_id
        LEFT JOIN town residence ON t.town_fk=residence.town_id
        LEFT JOIN religion ON t.religion_fk=religion.religion_id
        LEFT JOIN military_district ON t.military_district_fk=military_district_id
        LEFT JOIN corps posted_from_corps ON t.posted_corps_fk=posted_from_corps.corps_id
        LEFT JOIN rank ON t.rank_fk=rank.rank_id
        LEFT JOIN embarkation_unit ON t.embarkation_unit_fk=embarkation_unit.embarkation_unit_id
        LEFT JOIN section ON t.section_fk = section.section_id
        LEFT JOIN corps attached_corps ON t.attached_corps_fk=attached_corps.corps_id
        LEFT JOIN training ON embarkation_unit.training_fk=training.training_id
        LEFT JOIN training_location_type ON training.training_location_type=training_location_type.training_location_type_id
        LEFT JOIN transport ON embarkation_unit.transport_uk_fk=transport.transport_id
        LEFT JOIN transport_ref transport_uk_ref ON transport.transport_ref_fk=transport_uk_ref.transport_ref_id
        LEFT JOIN transport_vessel transport_uk_vessel ON transport.transport_vessel_fk=transport_uk_vessel.transport_vessel_id

        WHERE t.id=%s
    '''
    values = [id]
    tunneller_result = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = f'''
        SELECT army_experience_name, {country_col[lang]} AS country, {conflict_col[lang]} AS conflict_name, army_experience_in_month

        FROM army_experience_join

        LEFT JOIN army_experience ON army_experience.army_experience_id=army_experience_join.army_experience_c_id
        LEFT JOIN country ON country.country_id=army_experience_join.army_experience_c_c_id
        LEFT JOIN conflict ON conflict.conflict_id=army_experience_join.army_experience_w_id

        WHERE army_experience_join.army_experience_t_id=%s
    '''
    army_experience_result = run_sql(army_experience_sql, mysql, values)

    medals_sql = f'''
        SELECT {medal_name_col[lang]} AS medal_name, {medal_citation_col[lang]} AS medal_citation, {country_col[lang]} AS country

        FROM medal_join

        JOIN medal ON medal.medal_id=medal_m_id
        LEFT JOIN medal_citation ON medal_citation.medal_citation_id=medal_c_id
        LEFT JOIN country ON country.country_id=medal_m_c_id
        WHERE medal_join.medal_t_id=%s
    '''
    medals_result = run_sql(medals_sql, mysql, values)

    nz_archives_sql = 'SELECT nz_archives_ref, nz_archives_url FROM nz_archives LEFT JOIN tunneller ON tunneller.id=nz_archives.nz_archives_t_id WHERE tunneller.id=%s'
    nz_archives_result = run_sql(nz_archives_sql, mysql, values)

    london_gazette_sql = 'SELECT london_gazette_date, london_gazette_page FROM london_gazette_join JOIN london_gazette ON london_gazette.london_gazette_id=london_gazette_join.london_gazette_lg_id WHERE london_gazette_join.london_gazette_t_id=%s'
    london_gazette_result = run_sql(london_gazette_sql, mysql, values)

    image_source_book_id_sql = f'''
        SELECT book_id

        FROM tunneller
        
        LEFT JOIN book ON book.book_id=tunneller.image_source_book_fk
        WHERE id=%s
    '''
    image_source_book_id_result = run_sql(
        image_source_book_id_sql, mysql, values)

    def get_image_source_book_authors(image_source_book_id_result):
        if image_source_book_id_result != ():
            formatted_book_id = [
                str(image_source_book_id_result[0].get('book_id'))]
            image_authors_sql = 'SELECT author_forename, author_surname FROM author_book_join JOIN author ON author.author_id=author_book_join.author_book_a_id WHERE author_book_join.author_book_b_id=%s'
            image_authors_result = run_sql(
                image_authors_sql, mysql, formatted_book_id)
            return image_authors_result
        return []

    if tunneller_result is not None:

        # image_source_archives = Tunneller.get_image_source_archives(
        #     tunneller_result['archives_name'], tunneller_result['archives_ref'])
        # image_source_newspaper = Tunneller.get_image_source_newspaper(
        #     tunneller_result['newspaper_name'], Tunneller.get_date(tunneller_result['newspaper_date']))
        # image_source_book = Tunneller.get_image_source_book(get_image_source_book_authors(
        #     image_source_book_id_result), tunneller_result['book_title'], tunneller_result['book_town'], tunneller_result['book_publisher'], tunneller_result['book_year'], tunneller_result['book_page'])
        # image_source = Tunneller.get_image_source(Tunneller.get_image_source_auckland_libraries(
        #     tunneller_result['image_source_auckland_libraries']), image_source_archives, Tunneller.get_image_source_family(tunneller_result['family_name'], lang), image_source_newspaper, image_source_book)
        # image = Tunneller.get_image(Tunneller.get_image_url(
        #     tunneller_result['image']), image_source)

        # sources = Tunneller.get_sources(Tunneller.get_nz_archives(nz_archives_result), Tunneller.get_awmm(tunneller_result['awmm_cenotaph']), Tunneller.get_nominal_roll(
        #     tunneller_result['nominal_roll_volume'], tunneller_result['nominal_roll_number'], tunneller_result['nominal_roll_page'], lang), Tunneller.get_london_gazette(london_gazette_result))

        data = {
            'id': tunneller_result['id'],
            'serial': tunneller_result['serial'],
            'name': {'forename': tunneller_result['forename'], 'surname': tunneller_result['surname']},
            'origins': {
                'birth': {
                    'year': get_year(tunneller_result['birth_year'], format_date(tunneller_result['birth_date'])),
                    'date': format_date(tunneller_result['birth_date']),
                    'country': tunneller_result['birth_country']
                },
                'parents': {
                    'mother': get_parent(tunneller_result['mother_name'], tunneller_result['mother_origin']),
                    'father': get_parent(tunneller_result['father_name'], tunneller_result['father_origin'])
                },
                'nz_resident_in_month': get_nz_resident(tunneller_result['nz_resident_in_month'], lang)
            },
            'pre_war_years': {
                'marital_status': tunneller_result['marital_status'],
                'wife': tunneller_result['wife_name'],
                'employment': {
                    'occupation': tunneller_result['occupation'],
                    'employer': tunneller_result['employer']
                },
                'residence': tunneller_result['residence'],
                'religion': tunneller_result['religion'],
                'army_experience': map_army_experience(army_experience_result, lang)
            },
            'military_years': {
                'enlistment': {
                    'enlistment_date': format_date(tunneller_result['enlistment_date']),
                    'military_district': tunneller_result['military_district_name'],
                    'alias': tunneller_result['aka'],
                    'transferred_to_tunnellers': get_transferred_to_tunnellers(format_date(tunneller_result['posted_date']), tunneller_result['posted_from_corps']),
                    'rank': tunneller_result['rank']
                },
                'embarkation_unit': {
                    'detachment': get_detachment(tunneller_result['embarkation_unit'], lang),
                    'section': get_section(tunneller_result['section'], lang),
                    'attached_corps': tunneller_result['attached_corps'],
                    'training': get_training(format_date(tunneller_result['training_start']), tunneller_result['training_location'], tunneller_result['training_location_type'])
                },
                'transport_uk': {
                    'transport_reference': get_transport_reference(tunneller_result['transport_uk_ref'], lang),
                    'vessel': tunneller_result['transport_uk_vessel'],
                    'departure_date': format_date(tunneller_result['transport_uk_start']),
                    'departure_port': tunneller_result['transport_uk_origin'],
                    'arrival_date': format_date(tunneller_result['transport_uk_end']),
                    'arrival_port': tunneller_result['transport_uk_destination']
                },
                'medals': map_medals(medals_result)
            }
        }
        tunneller = from_dict(data_class=Tunneller, data=data)

    return tunneller
