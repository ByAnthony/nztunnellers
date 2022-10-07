from db.run_sql import run_sql
from models.tunneller import Tunneller
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

    tunneller = None

    tunneller_sql = f'''
        SELECT id, forename, surname, aka, serial, {rank_col[lang]} AS rank, {embarkation_unit_col[lang]} AS embarkation_unit, training.training_start, training.training_location, {training_location_type_col[lang]} AS training_location_type, transport_uk.transport_uk_ref, transport_uk.transport_uk_vessel, transport_uk.transport_uk_start, transport_uk.transport_uk_origin, transport_uk.transport_uk_end, transport_uk.transport_uk_destination, {section_col[lang]} AS section, {attached_corps_col[lang]} AS attached_corps, birth_date, birth_year, {birth_country_col[lang]} AS birth_country, mother_name, {mother_origin_col[lang]} AS mother_origin, father_name, {father_origin_col[lang]} AS father_origin, nz_resident_in_month, {marital_status_col[lang]} AS marital_status, wife_name, {occupation_col[lang]} AS occupation, last_employer_name, town_name, {religion_col[lang]} AS religion, enlistment_date, military_district_name, posted_date, {posted_from_corps_col[lang]} AS posted_from_corps, awmm_cenotaph, nominal_roll.nominal_roll_volume, nominal_roll.nominal_roll_number, nominal_roll.nominal_roll_page, image, image_source_auckland_libraries, archives_name, archives_ref, family_name, newspaper_name, newspaper_date, book_title, book_town, book_publisher, book_year, book_page

        FROM tunneller t

        LEFT JOIN rank ON t.rank_fk=rank.rank_id
        LEFT JOIN embarkation_unit ON t.embarkation_unit_fk=embarkation_unit.embarkation_unit_id
        LEFT JOIN training ON embarkation_unit.training_fk=training.training_id
        LEFT JOIN training_location_type ON training.training_location_type=training_location_type.training_location_type_id
        LEFT JOIN transport_uk ON embarkation_unit.transport_uk_fk=transport_uk.transport_uk_id
        LEFT JOIN section ON t.section_fk = section.section_id
        LEFT JOIN corps attached_corps ON t.attached_corps_fk=attached_corps.corps_id
        LEFT JOIN country birth_country ON t.birth_country_fk=birth_country.country_id
        LEFT JOIN country mother_origin ON t.mother_origin_fk=mother_origin.country_id
        LEFT JOIN country father_origin ON t.father_origin_fk=father_origin.country_id
        LEFT JOIN marital_status ON t.marital_status_fk=marital_status.marital_status_id
        LEFT JOIN occupation ON t.occupation_fk=occupation.occupation_id
        LEFT JOIN last_employer ON t.last_employer_fk=last_employer.last_employer_id
        LEFT JOIN town ON t.town_fk=town.town_id
        LEFT JOIN religion ON t.religion_fk=religion.religion_id
        LEFT JOIN military_district ON t.military_district_fk=military_district.military_district_id
        LEFT JOIN corps posted_from_corps ON t.posted_corps_fk=posted_from_corps.corps_id
        LEFT JOIN nominal_roll ON t.nominal_roll_fk=nominal_roll.nominal_roll_id
        LEFT JOIN archives ON archives.archives_id=t.image_source_archives_fk
        LEFT JOIN archives_name ON archives_name.archives_name_id=archives.archives_name_fk
        LEFT JOIN family ON family.family_id=t.image_source_family_fk
        LEFT JOIN newspaper ON newspaper.newspaper_id=t.image_source_newspaper_fk
        LEFT JOIN newspaper_name ON newspaper_name.newspaper_name_id=newspaper.newspaper_name_fk
        LEFT JOIN book ON book.book_id=t.image_source_book_fk

        WHERE id=%s'''
    values = [id]
    tunneller_result = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = f'''
        SELECT army_experience_name, {country_col[lang]} AS country, {conflict_col[lang]} AS conflict_name, army_experience_in_month
        FROM army_experience_join
        LEFT JOIN army_experience ON army_experience.army_experience_id=army_experience_join.army_experience_c_id
        LEFT JOIN country ON country.country_id=army_experience_join.army_experience_c_c_id
        LEFT JOIN conflict ON conflict.conflict_id=army_experience_join.army_experience_w_id
        WHERE army_experience_join.army_experience_t_id=%s'''
    army_experience_result = run_sql(army_experience_sql, mysql, values)

    medals_sql = f'''
        SELECT {medal_name_col[lang]} AS medal_name, {medal_citation_col[lang]} AS medal_citation, {country_col[lang]} AS country
        FROM medal_join 
        JOIN medal ON medal.medal_id=medal_m_id 
        LEFT JOIN medal_citation ON medal_citation.medal_citation_id=medal_c_id
        LEFT JOIN country ON country.country_id=medal_m_c_id
        WHERE medal_join.medal_t_id=%s'''
    medals_result = run_sql(medals_sql, mysql, values)

    nz_archives_sql = 'SELECT nz_archives_ref, nz_archives_url FROM nz_archives LEFT JOIN tunneller ON tunneller.id=nz_archives.nz_archives_t_id WHERE tunneller.id=%s'
    nz_archives_result = run_sql(nz_archives_sql, mysql, values)

    london_gazette_sql = 'SELECT london_gazette_date, london_gazette_page FROM london_gazette_join JOIN london_gazette ON london_gazette.london_gazette_id=london_gazette_join.london_gazette_lg_id WHERE london_gazette_join.london_gazette_t_id=%s'
    london_gazette_result = run_sql(london_gazette_sql, mysql, values)

    image_source_book_id_sql = f'''
        SELECT book_id
        FROM tunneller
        LEFT JOIN book ON book.book_id=tunneller.image_source_book_fk
        WHERE id=%s'''
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

        name = Tunneller.get_name(
            tunneller_result['forename'],
            tunneller_result['surname']
        )

        birth_date = Tunneller.get_birth_date(
            tunneller_result['birth_date']
        )
        birth_year = Tunneller.get_birth_year(
            tunneller_result['birth_year'],
            birth_date
        )
        birth_country = Tunneller.get_birth_country(
            tunneller_result['birth_country']
        )

        birth_info = Tunneller.get_birth_info(
            birth_year,
            birth_date,
            birth_country
        )

        mother = Tunneller.get_parent(
            tunneller_result['mother_name'],
            tunneller_result['mother_origin']
        )
        father = Tunneller.get_parent(
            tunneller_result['father_name'],
            tunneller_result['father_origin']
        )

        nz_resident = Tunneller.get_nz_resident(
            tunneller_result['nz_resident_in_month'],
            lang
        )

        origins = Tunneller.get_origins(
            birth_info,
            mother,
            father,
            nz_resident
        )

        marital_status = Tunneller.get_marital_status(
            tunneller_result['marital_status'],
            tunneller_result['wife_name']
        )

        occupation = Tunneller.get_occupation(
            tunneller_result['occupation'],
            tunneller_result['last_employer_name']
        )

        residence = Tunneller.get_residence(
            tunneller_result['town_name']
        )

        religion = Tunneller.get_religion(
            tunneller_result['religion']
        )

        army_experience = Tunneller.get_army_experience(
            army_experience_result,
            lang
        )

        pre_war_life = Tunneller.get_pre_war_life(
            marital_status,
            occupation,
            residence,
            religion,
            army_experience
        )

        enlistment_date = Tunneller.get_enlistment_date(
            tunneller_result['enlistment_date']
        )

        military_district = Tunneller.get_military_district(
            tunneller_result['military_district_name']
        )

        alias = Tunneller.get_alias(
            tunneller_result['aka']
        )

        posted_date = Tunneller.get_posted_date(
            tunneller_result['posted_date']
        )

        posted_from = Tunneller.get_posted_from(
            tunneller_result['posted_from_corps']
        )

        rank = Tunneller.get_rank(
            tunneller_result['rank']
        )

        enlistment = Tunneller.get_enlistment(
            enlistment_date,
            military_district,
            alias,
            posted_date,
            posted_from,
            rank
        )

        transport_reference_uk = Tunneller.get_transport_reference_uk(
            tunneller_result['transport_uk_ref'], lang
        )

        vessel_uk = Tunneller.get_vessel_uk(
            tunneller_result['transport_uk_vessel']
        )

        departure_uk_date = Tunneller.get_departure_uk_date(
            tunneller_result['transport_uk_start']
        )

        departure_uk_port = Tunneller.get_departure_uk_port(
            tunneller_result['transport_uk_origin']
        )

        arrival_uk_date = Tunneller.get_arrival_uk_date(
            tunneller_result['transport_uk_end']
        )

        arrival_uk_port = Tunneller.get_arrival_uk_port(
            tunneller_result['transport_uk_destination']
        )

        transport_uk = Tunneller.get_transport_uk(
            transport_reference_uk,
            vessel_uk,
            departure_uk_date,
            departure_uk_port,
            arrival_uk_date,
            arrival_uk_port
        )

        medals = Tunneller.get_medals(
            medals_result
        )

        military_life = Tunneller.get_military_life(
            enlistment,
            transport_uk,
            medals
        )

        tunneller = Tunneller(
            tunneller_result['id'],
            tunneller_result['serial'],
            name,
            origins,
            pre_war_life,
            military_life
        )

    return tunneller
