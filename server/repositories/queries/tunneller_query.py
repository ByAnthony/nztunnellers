# -*- coding: utf-8 -*-
from ...repositories.translations.translations import (
    attached_corps_col,
    birth_country_col,
    embarkation_unit_col,
    father_origin_col,
    marital_status_col,
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


def tunneller_query(lang: str) -> str:
    return f"""SELECT
        t.id
        , t.forename
        , t.surname
        , t.aka
        , t.serial
        , DATE_FORMAT(t.birth_date, '%%Y-%%m-%%d') AS birth_date
        , t.birth_year
        , {birth_country_col[lang]} AS birth_country
        , t.mother_name
        , {mother_origin_col[lang]} AS mother_origin
        , t.father_name
        , {father_origin_col[lang]} AS father_origin
        , CONVERT(t.nz_resident_in_month, char) AS nz_resident_in_month
        , {marital_status_col[lang]} AS marital_status
        , t.wife_name
        , {occupation_col[lang]} AS occupation
        , employer.last_employer_name AS employer
        , residence.town_name AS residence
        , {religion_col[lang]} AS religion
        , DATE_FORMAT(t.enlistment_date, '%%Y-%%m-%%d') AS enlistment_date
        , t.enlistment_year
        , military_district.military_district_name
        , t.aka
        , DATE_FORMAT(t.posted_date, '%%Y-%%m-%%d') AS posted_date
        , t.posted_year
        , {posted_from_corps_col[lang]} AS posted_from_corps
        , {rank_col[lang]} AS rank
        , {embarkation_unit_col[lang]} AS embarkation_unit
        , {section_col[lang]} AS section
        , {attached_corps_col[lang]} AS attached_corps
        , DATE_FORMAT(training.training_start, '%%Y-%%m-%%d') AS training_start
        , training.training_location
        , {training_location_type_col[lang]} AS training_location_type
        , transport_uk_ref.transport_ref_name AS transport_uk_ref
        , transport_uk_vessel.transport_vessel_name AS transport_uk_vessel
        , DATE_FORMAT(transport_uk.transport_start, '%%Y-%%m-%%d') AS transport_uk_start
        , transport_uk.transport_origin AS transport_uk_origin
        , DATE_FORMAT(transport_uk.transport_end, '%%Y-%%m-%%d') AS transport_uk_end
        , transport_uk.transport_destination AS transport_uk_destination
        , t.has_deserted
        , DATE_FORMAT(transferred.transferred_date, '%%Y-%%m-%%d') AS transferred_to_date
        , {transferred_to_col[lang]} AS transferred_to_unit
        , death_type.death_type_en AS death_type
        , DATE_FORMAT(t.death_date, '%%Y-%%m-%%d') AS death_date
        , t.death_year
        , {death_location_col[lang]} AS death_location
        , death_town.town_name AS death_town
        , {death_country_col[lang]} AS death_country
        , {death_cause_col[lang]} AS death_cause
        , {death_circumstances_col[lang]} AS death_circumstances
        , {cemetery_col[lang]} AS cemetery
        , cemetery_town.town_name AS cemetery_town
        , {cemetery_country_col[lang]} AS cemetery_country
        , t.grave_reference AS grave
        , transport_nz_ref.transport_ref_name AS transport_nz_ref
        , transport_nz_vessel.transport_vessel_name AS transport_nz_vessel
        , DATE_FORMAT(transport_nz.transport_start, '%%Y-%%m-%%d') AS transport_nz_start
        , transport_nz.transport_origin AS transport_nz_origin
        , DATE_FORMAT(transport_nz.transport_end, '%%Y-%%m-%%d') AS transport_nz_end
        , transport_nz.transport_destination AS transport_nz_destination
        , DATE_FORMAT(t.service_end, '%%Y-%%m-%%d') AS demobilization_date
        , t.discharge_uk
        , image
        , image_source_auckland_libraries
        , archives_name.archives_name
        , archives.archives_ref
        , family.family_name, newspaper_name.newspaper_name
        , DATE_FORMAT(newspaper.newspaper_date, '%%Y-%%m-%%d') AS newspaper_date
        , book.book_title
        , book.book_town
        , book.book_publisher
        , book.book_year
        , book.book_page
        , awmm_cenotaph
        , nominal_roll.nominal_roll_volume
        , nominal_roll.nominal_roll_number
        , nominal_roll.nominal_roll_page


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
        LEFT JOIN death_type ON t.death_type_fk=death_type.death_type_id
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
