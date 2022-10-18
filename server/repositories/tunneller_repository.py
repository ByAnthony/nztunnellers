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
        SELECT id, forename, surname, aka, serial, {rank_col[lang]} AS rank, {embarkation_unit_col[lang]} AS embarkation_unit, training.training_start, training.training_location, {training_location_type_col[lang]} AS training_location_type, transport_ref.transport_ref_name AS transport_uk_ref, transport_vessel.transport_vessel_name AS transport_uk_vessel, transport.transport_start AS transport_uk_start, transport.transport_origin AS transport_uk_origin, transport.transport_end AS transport_uk_end, transport.transport_destination AS transport_uk_destination, {section_col[lang]} AS section, {attached_corps_col[lang]} AS attached_corps, birth_date, birth_year, {birth_country_col[lang]} AS birth_country, mother_name, {mother_origin_col[lang]} AS mother_origin, father_name, {father_origin_col[lang]} AS father_origin, nz_resident_in_month, {marital_status_col[lang]} AS marital_status, wife_name, {occupation_col[lang]} AS occupation, last_employer_name, town_name, {religion_col[lang]} AS religion, enlistment_date, military_district_name, posted_date, {posted_from_corps_col[lang]} AS posted_from_corps, has_deserted, awmm_cenotaph, nominal_roll.nominal_roll_volume, nominal_roll.nominal_roll_number, nominal_roll.nominal_roll_page, image, image_source_auckland_libraries, archives_name, archives_ref, family_name, newspaper_name, newspaper_date, book_title, book_town, book_publisher, book_year, book_page

        FROM tunneller t

        LEFT JOIN rank ON t.rank_fk=rank.rank_id
        LEFT JOIN embarkation_unit ON t.embarkation_unit_fk=embarkation_unit.embarkation_unit_id
        LEFT JOIN training ON embarkation_unit.training_fk=training.training_id
        LEFT JOIN training_location_type ON training.training_location_type=training_location_type.training_location_type_id
        LEFT JOIN transport ON embarkation_unit.transport_uk_fk=transport.transport_id
        LEFT JOIN transport_ref ON transport.transport_ref=transport_ref.transport_ref_id
        LEFT JOIN transport_vessel ON transport.transport_vessel=transport_vessel_id
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
            tunneller_result['forename'], tunneller_result['surname'])

        birth_date = Tunneller.get_date(tunneller_result['birth_date'])
        birth_year = Tunneller.get_year(
            tunneller_result['birth_year'], birth_date)
        birth_details = Tunneller.get_birth_details(
            birth_year, birth_date, Tunneller.get_country(tunneller_result['birth_country']))
        parents = Tunneller.get_parents(Tunneller.get_parent(tunneller_result['mother_name'], tunneller_result['mother_origin']), Tunneller.get_parent(
            tunneller_result['father_name'], tunneller_result['father_origin']))
        origins = Tunneller.get_origins(
            birth_details, parents, Tunneller.get_nz_resident(tunneller_result['nz_resident_in_month'], lang))

        marital_status = Tunneller.get_marital_status(
            tunneller_result['marital_status'])
        wife = Tunneller.get_wife(tunneller_result['wife_name'])
        employment = Tunneller.get_employment(Tunneller.get_occupation(
            tunneller_result['occupation']), Tunneller.get_employer(tunneller_result['last_employer_name']))
        pre_war_years = Tunneller.get_pre_war_years(
            marital_status, wife, employment, Tunneller.get_town(tunneller_result['town_name']), Tunneller.get_religion(tunneller_result['religion']), Tunneller.get_army_experience(army_experience_result, lang))

        transferred_to_tunnellers = Tunneller.get_transferred_to_tunnellers(Tunneller.get_date(
            tunneller_result['posted_date']), Tunneller.get_posted_from(tunneller_result['posted_from_corps']))
        enlistment = Tunneller.get_enlistment(Tunneller.get_date(tunneller_result['enlistment_date']), Tunneller.get_military_district(
            tunneller_result['military_district_name']), Tunneller.get_alias(tunneller_result['aka']), transferred_to_tunnellers, Tunneller.get_rank(tunneller_result['rank']))
        training = Tunneller.get_training(Tunneller.get_date(tunneller_result['training_start']), Tunneller.get_training_location(
            tunneller_result['training_location']), Tunneller.get_training_location_type(tunneller_result['training_location_type']))
        embarkation_unit = Tunneller.get_embarkation_unit(Tunneller.get_detachment(tunneller_result['embarkation_unit'], lang), Tunneller.get_section(
            tunneller_result['section'], lang), Tunneller.get_attached_corps(tunneller_result['attached_corps']), training)
        transport_uk = Tunneller.get_transport_uk(Tunneller.get_transport_reference_uk(tunneller_result['transport_uk_ref'], lang), Tunneller.get_vessel_uk(tunneller_result['transport_uk_vessel']), Tunneller.get_date(
            tunneller_result['transport_uk_start']), Tunneller.get_town(tunneller_result['transport_uk_origin']), Tunneller.get_date(tunneller_result['transport_uk_end']), Tunneller.get_town(tunneller_result['transport_uk_destination']))
        end_of_service = Tunneller.get_end_of_service(
            Tunneller.get_end_of_service_as_deserter(tunneller_result['has_deserted'], lang))
        military_years = Tunneller.get_military_years(
            enlistment, embarkation_unit, transport_uk, end_of_service, Tunneller.get_medals(medals_result))

        image_source_archives = Tunneller.get_image_source_archives(
            tunneller_result['archives_name'], tunneller_result['archives_ref'])
        image_source_newspaper = Tunneller.get_image_source_newspaper(
            tunneller_result['newspaper_name'], Tunneller.get_date(tunneller_result['newspaper_date']))
        image_source_book = Tunneller.get_image_source_book(get_image_source_book_authors(
            image_source_book_id_result), tunneller_result['book_title'], tunneller_result['book_town'], tunneller_result['book_publisher'], tunneller_result['book_year'], tunneller_result['book_page'])
        image_source = Tunneller.get_image_source(Tunneller.get_image_source_auckland_libraries(
            tunneller_result['image_source_auckland_libraries']), image_source_archives, Tunneller.get_image_source_family(tunneller_result['family_name'], lang), image_source_newspaper, image_source_book)
        image = Tunneller.get_image(Tunneller.get_image_url(
            tunneller_result['image']), image_source)

        sources = Tunneller.get_sources(Tunneller.get_nz_archives(nz_archives_result), Tunneller.get_awmm(tunneller_result['awmm_cenotaph']), Tunneller.get_nominal_roll(
            tunneller_result['nominal_roll_volume'], tunneller_result['nominal_roll_number'], tunneller_result['nominal_roll_page'], lang), Tunneller.get_london_gazette(london_gazette_result))

        tunneller = Tunneller(
            tunneller_result['id'], tunneller_result['serial'], name, origins, pre_war_years, military_years, image, sources)

    return tunneller
