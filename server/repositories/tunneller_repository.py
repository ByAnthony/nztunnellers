# -*- coding: utf-8 -*-
from dacite import from_dict
from ..models.helpers.translator_helpers import translate_town
from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.helpers.date_helpers import (
    format_date_to_day_month_and_year,
    get_birth_date,
    get_date,
)
from ..models.helpers.image_helpers import (
    get_image,
    get_image_source,
    get_image_source_archives,
    get_image_source_auckland_libraries,
    get_image_source_book,
    get_image_source_family,
    get_image_source_newspaper,
    get_image_url,
)
from ..models.helpers.military_years_helpers import (
    get_boolean,
    get_cemetery,
    get_death_circumstances,
    get_death_place,
    get_death_war,
    get_detachment,
    get_end_of_service,
    get_end_of_service_country,
    get_section,
    get_training,
    get_transferred_to,
    get_transferred_to_tunnellers,
    get_transport_nz,
    get_transport_reference,
    map_medals,
)
from ..models.helpers.origins_helpers import get_nz_resident, get_parent
from ..models.helpers.pre_war_years_helpers import map_army_experience
from ..models.helpers.sources_helpers import (
    get_awmm,
    get_nominal_roll,
    map_london_gazette,
    map_nz_archives,
)
from ..models.image import ImageBookAuthors
from ..models.military_years import Medal
from ..models.pre_war_years import ArmyExperience
from ..models.sources import LondonGazette, NewZealandArchives
from ..models.tunneller import Tunneller

from .translations.translations import (
    attached_corps_col,
    birth_country_col,
    conflict_col,
    country_col,
    embarkation_unit_col,
    father_origin_col,
    marital_status_col,
    medal_citation_col,
    medal_name_col,
    mother_origin_col,
    occupation_col,
    posted_from_corps_col,
    rank_col,
    religion_col,
    section_col,
    training_location_type_col,
    transferred_to_col,
    death_location_col,
    death_country_col,
    death_cause_col,
    cemetery_col,
    cemetery_country_col,
    death_circumstances_col,
)


def show(id: int, lang: str, mysql: MySQL) -> Tunneller:

    tunneller_sql = f"""SELECT t.id,
        t.forename,
        t.surname,
        t.aka,
        t.serial,
        DATE_FORMAT(t.birth_date, '%%Y-%%m-%%d') AS birth_date,
        DATE_FORMAT(t.birth_year, '%%Y-%%m-%%d') AS birth_year,
        {birth_country_col[lang]} AS birth_country,
        t.mother_name,
        {mother_origin_col[lang]} AS mother_origin,
        t.father_name, {father_origin_col[lang]} AS father_origin,
        CONVERT(t.nz_resident_in_month, char) AS nz_resident_in_month,
        {marital_status_col[lang]} AS marital_status,
        t.wife_name, {occupation_col[lang]} AS occupation,
        employer.last_employer_name AS employer,
        residence.town_name AS residence,
        {religion_col[lang]} AS religion,
        DATE_FORMAT(t.enlistment_date, '%%Y-%%m-%%d') AS enlistment_date,
        military_district.military_district_name,
        t.aka,
        DATE_FORMAT(t.posted_date, '%%Y-%%m-%%d') AS posted_date,
        {posted_from_corps_col[lang]} AS posted_from_corps,
        {rank_col[lang]} AS rank,
        {embarkation_unit_col[lang]} AS embarkation_unit,
        {section_col[lang]} AS section,
        {attached_corps_col[lang]} AS attached_corps,
        DATE_FORMAT(training.training_start, '%%Y-%%m-%%d') AS training_start,
        training.training_location,
        {training_location_type_col[lang]} AS training_location_type,
        transport_uk_ref.transport_ref_name AS transport_uk_ref,
        transport_uk_vessel.transport_vessel_name AS transport_uk_vessel,
        DATE_FORMAT(transport_uk.transport_start, '%%Y-%%m-%%d') AS transport_uk_start,
        transport_uk.transport_origin AS transport_uk_origin,
        DATE_FORMAT(transport_uk.transport_end, '%%Y-%%m-%%d') AS transport_uk_end,
        transport_uk.transport_destination AS transport_uk_destination,
        has_deserted,
        DATE_FORMAT(transferred.transferred_date, '%%Y-%%m-%%d') AS transferred_to_date,
        {transferred_to_col[lang]} AS transferred_to_unit,
        t.death_type_fk AS death_type,
        DATE_FORMAT(t.death_date, '%%Y-%%m-%%d') AS death_date,
        DATE_FORMAT(t.death_year, '%%Y-%%m-%%d') AS death_year,
        {death_location_col[lang]} AS death_location,
        death_town.town_name AS death_town,
        {death_country_col[lang]} AS death_country,
        {death_cause_col[lang]} AS death_cause,
        {death_circumstances_col[lang]} AS death_circumstances,
        {cemetery_col[lang]} AS cemetery,
        cemetery_town.town_name AS cemetery_town,
        {cemetery_country_col[lang]} AS cemetery_country,
        t.grave_reference AS grave,
        transport_nz_ref.transport_ref_name AS transport_nz_ref,
        transport_nz_vessel.transport_vessel_name AS transport_nz_vessel,
        DATE_FORMAT(transport_nz.transport_start, '%%Y-%%m-%%d') AS transport_nz_start,
        transport_nz.transport_origin AS transport_nz_origin,
        DATE_FORMAT(transport_nz.transport_end, '%%Y-%%m-%%d') AS transport_nz_end,
        transport_nz.transport_destination AS transport_nz_destination,
        DATE_FORMAT(t.service_end, '%%Y-%%m-%%d') AS demobilization_date,
        t.discharge_uk,
        image,
        image_source_auckland_libraries,
        archives_name.archives_name,
        archives.archives_ref,
        family.family_name, newspaper_name.newspaper_name,
        DATE_FORMAT(newspaper.newspaper_date, '%%Y-%%m-%%d') AS newspaper_date,
        book.book_title,
        book.book_town,
        book.book_publisher,
        book.book_year,
        book.book_page,
        awmm_cenotaph,
        nominal_roll.nominal_roll_volume,
        nominal_roll.nominal_roll_number,
        nominal_roll.nominal_roll_page

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
        LEFT JOIN training_location_type
        ON training.training_location_type=training_location_type.training_location_type_id
        LEFT JOIN transport transport_uk ON embarkation_unit.transport_uk_fk=transport_uk.transport_id
        LEFT JOIN transport_ref transport_uk_ref ON transport_uk.transport_ref_fk=transport_uk_ref.transport_ref_id
        LEFT JOIN transport_vessel transport_uk_vessel
        ON transport_uk.transport_vessel_fk=transport_uk_vessel.transport_vessel_id
        LEFT JOIN transferred ON transferred.transferred_id=t.transferred_fk
        LEFT JOIN transferred_to ON transferred_to.transferred_to_id=transferred.transferred_to_fk
        LEFT JOIN death_location ON t.death_location_fk=death_location.death_location_id
        LEFT JOIN town death_town ON t.death_town_fk=death_town.town_id
        LEFT JOIN country death_country ON death_town.town_country_fk=death_country.country_id
        LEFT JOIN death_cause ON t.death_cause_fk=death_cause.death_cause_id
        LEFT JOIN death_circumstances ON t.death_circumstances_fk=death_circumstances.death_circumstances_id
        LEFT JOIN cemetery ON t.cemetery_fk=cemetery.cemetery_id
        LEFT JOIN town cemetery_town ON cemetery.cemetery_town_fk=cemetery_town.town_id
        LEFT JOIN country cemetery_country ON cemetery_town.town_country_fk=cemetery_country.country_id
        LEFT JOIN transport transport_nz ON t.transport_nz_fk=transport_nz.transport_id
        LEFT JOIN transport_ref transport_nz_ref ON transport_nz.transport_ref_fk=transport_nz_ref.transport_ref_id
        LEFT JOIN transport_vessel transport_nz_vessel
        ON transport_nz.transport_vessel_fk=transport_nz_vessel.transport_vessel_id
        LEFT JOIN nominal_roll ON t.nominal_roll_fk=nominal_roll.nominal_roll_id
        LEFT JOIN archives ON archives.archives_id=t.image_source_archives_fk
        LEFT JOIN archives_name ON archives_name.archives_name_id=archives.archives_name_fk
        LEFT JOIN family ON family.family_id=t.image_source_family_fk
        LEFT JOIN newspaper ON newspaper.newspaper_id=t.image_source_newspaper_fk
        LEFT JOIN newspaper_name ON newspaper_name.newspaper_name_id=newspaper.newspaper_name_fk
        LEFT JOIN book ON book.book_id=t.image_source_book_fk

        WHERE t.id=%s"""
    values = [id]
    tunneller_result: Tunneller = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = f"""SELECT army_experience.army_experience_name AS unit, {country_col[lang]} AS country,
        {conflict_col[lang]} AS conflict, CONVERT(army_experience_join.army_experience_in_month, char) AS duration

        FROM army_experience

        LEFT JOIN army_experience_join ON army_experience_join.army_experience_c_id=army_experience.army_experience_id
        LEFT JOIN country ON country.country_id=army_experience_join.army_experience_c_c_id
        LEFT JOIN conflict ON conflict.conflict_id=army_experience_join.army_experience_w_id

        WHERE army_experience_join.army_experience_t_id=%s"""
    army_experience_result: list[ArmyExperience] = run_sql(
        army_experience_sql, mysql, values
    )

    medals_sql = f"""SELECT {medal_name_col[lang]} AS name, {country_col[lang]} AS country,
        {medal_citation_col[lang]} AS citation

        FROM medal

        JOIN medal_join ON medal_join.medal_m_id=medal.medal_id
        LEFT JOIN medal_citation ON medal_citation.medal_citation_id=medal_c_id
        LEFT JOIN country ON country.country_id=medal_m_c_id

        WHERE medal_join.medal_t_id=%s"""
    medals_result: list[Medal] = run_sql(medals_sql, mysql, values)

    nz_archives_sql = """SELECT nz_archives.nz_archives_ref AS reference, nz_archives.nz_archives_url AS url
        FROM nz_archives
        LEFT JOIN tunneller ON tunneller.id=nz_archives.nz_archives_t_id
        WHERE tunneller.id=%s"""
    nz_archives_result: list[NewZealandArchives] = run_sql(
        nz_archives_sql, mysql, values
    )

    london_gazette_sql = """SELECT london_gazette.london_gazette_page AS page,
        DATE_FORMAT(london_gazette.london_gazette_date, '%%Y-%%m-%%d') AS date
        FROM london_gazette
        JOIN london_gazette_join ON london_gazette_join.london_gazette_lg_id=london_gazette.london_gazette_id
        WHERE london_gazette_join.london_gazette_t_id=%s"""
    london_gazette_result: list[LondonGazette] = run_sql(
        london_gazette_sql, mysql, values
    )

    book_authors_sql = """SELECT book.book_id, author.author_forename AS forename, author.author_surname AS surname

        FROM author_book_join

        LEFT JOIN author ON author.author_id=author_book_join.author_book_a_id
        LEFT JOIN book ON author_book_join.author_book_b_id=book.book_id
        LEFT JOIN tunneller ON book.book_id=tunneller.image_source_book_fk

        WHERE tunneller.id=%s"""
    book_authors_result: list[ImageBookAuthors] = run_sql(
        book_authors_sql, mysql, values
    )

    if tunneller_result is not None:

        data = {
            "id": tunneller_result["id"],
            "serial": tunneller_result["serial"],
            "name": {
                "forename": tunneller_result["forename"],
                "surname": tunneller_result["surname"],
            },
            "origins": {
                "birth": {
                    "date": get_birth_date(
                        tunneller_result["birth_year"],
                        tunneller_result["birth_date"],
                        lang,
                    ),
                    "country": tunneller_result["birth_country"],
                },
                "parents": {
                    "mother": get_parent(
                        tunneller_result["mother_name"],
                        tunneller_result["mother_origin"],
                    ),
                    "father": get_parent(
                        tunneller_result["father_name"],
                        tunneller_result["father_origin"],
                    ),
                },
                "in_nz_length": get_nz_resident(
                    tunneller_result["nz_resident_in_month"], lang
                ),
            },
            "pre_war_years": {
                "army_experience": map_army_experience(army_experience_result, lang),
                "employment": {
                    "occupation": tunneller_result["occupation"],
                    "employer": tunneller_result["employer"],
                },
                "residence": tunneller_result["residence"],
                "marital_status": tunneller_result["marital_status"],
                "wife": tunneller_result["wife_name"],
                "religion": tunneller_result["religion"],
            },
            "military_years": {
                "enlistment": {
                    "rank": tunneller_result["rank"],
                    "date": get_date(tunneller_result["enlistment_date"], lang),
                    "district": tunneller_result["military_district_name"],
                    "alias": tunneller_result["aka"],
                    "transferred_to_tunnellers": get_transferred_to_tunnellers(
                        get_date(tunneller_result["posted_date"], lang),
                        tunneller_result["posted_from_corps"],
                    ),
                },
                "embarkation_unit": {
                    "training": get_training(
                        get_date(tunneller_result["training_start"], lang),
                        tunneller_result["training_location"],
                        tunneller_result["training_location_type"],
                    ),
                    "detachment": get_detachment(
                        tunneller_result["embarkation_unit"], lang
                    ),
                    "section": get_section(tunneller_result["section"], lang),
                    "attached_corps": tunneller_result["attached_corps"],
                },
                "transport_uk": {
                    "reference": get_transport_reference(
                        tunneller_result["transport_uk_ref"], lang
                    ),
                    "vessel": tunneller_result["transport_uk_vessel"],
                    "departure_date": get_date(
                        tunneller_result["transport_uk_start"], lang
                    ),
                    "departure_port": tunneller_result["transport_uk_origin"],
                    "arrival_date": get_date(
                        tunneller_result["transport_uk_end"], lang
                    ),
                    "arrival_port": tunneller_result["transport_uk_destination"],
                },
                "end_of_service": {
                    "deserter": get_boolean(tunneller_result["has_deserted"]),
                    "transferred": get_transferred_to(
                        tunneller_result["transferred_to_date"],
                        tunneller_result["transferred_to_unit"],
                        lang,
                    ),
                    "death_war": get_death_war(
                        tunneller_result["death_type"],
                        get_birth_date(
                            tunneller_result["death_year"],
                            tunneller_result["death_date"],
                            lang,
                        ),
                        get_death_place(
                            tunneller_result["death_location"],
                            translate_town(tunneller_result["death_town"], lang),
                            tunneller_result["death_country"],
                        ),
                        get_death_circumstances(
                            tunneller_result["death_cause"],
                            tunneller_result["death_circumstances"],
                        ),
                        get_cemetery(
                            tunneller_result["cemetery"],
                            tunneller_result["cemetery_town"],
                            tunneller_result["cemetery_country"],
                            tunneller_result["grave"],
                        ),
                    ),
                    "transport_nz": get_transport_nz(
                        get_transport_reference(
                            tunneller_result["transport_nz_ref"], lang
                        ),
                        tunneller_result["transport_nz_vessel"],
                        get_date(tunneller_result["transport_nz_start"], lang),
                        tunneller_result["transport_nz_origin"],
                        get_date(tunneller_result["transport_nz_end"], lang),
                        tunneller_result["transport_nz_destination"],
                    ),
                    "demobilization": get_end_of_service(
                        get_date(tunneller_result["demobilization_date"], lang),
                        get_end_of_service_country(
                            tunneller_result["discharge_uk"], lang
                        ),
                    ),
                },
                "medals": map_medals(medals_result),
            },
            "post_service_years": {},
            "sources": {
                "nz_archives": map_nz_archives(nz_archives_result),
                "awmm_cenotaph": get_awmm(tunneller_result["awmm_cenotaph"]),
                "nominal_roll": get_nominal_roll(
                    tunneller_result["nominal_roll_volume"],
                    tunneller_result["nominal_roll_number"],
                    tunneller_result["nominal_roll_page"],
                    lang,
                ),
                "london_gazette": map_london_gazette(london_gazette_result, lang),
            },
            "image": get_image(
                get_image_url(tunneller_result["image"]),
                get_image_source(
                    get_image_source_auckland_libraries(
                        tunneller_result["image_source_auckland_libraries"]
                    ),
                    get_image_source_archives(
                        tunneller_result["archives_name"],
                        tunneller_result["archives_ref"],
                    ),
                    get_image_source_family(tunneller_result["family_name"], lang),
                    get_image_source_newspaper(
                        tunneller_result["newspaper_name"],
                        format_date_to_day_month_and_year(
                            tunneller_result["newspaper_date"], lang
                        ),
                    ),
                    get_image_source_book(
                        book_authors_result,
                        tunneller_result["book_title"],
                        tunneller_result["book_town"],
                        tunneller_result["book_publisher"],
                        tunneller_result["book_year"],
                        tunneller_result["book_page"],
                    ),
                ),
            ),
        }

        tunneller: Tunneller = from_dict(data_class=Tunneller, data=data)

        return tunneller
