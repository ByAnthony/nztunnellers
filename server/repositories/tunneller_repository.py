from db.run_sql import run_sql


rank_col = {'en': 'rank_en', 'fr': 'rank_fr'}


def show(id, lang, mysql):
    tunneller_sql = f'''
        SELECT id, surname, forename, aka, serial, {rank_col[lang]} AS rank, embarkation_unit.embarkation_unit_en, training.training_start, training.training_location, training_location_type.training_location_type_en, transport_uk.transport_uk_ref, transport_uk.transport_uk_vessel, transport_uk.transport_uk_start, transport_uk.transport_uk_origin, transport_uk.transport_uk_end, transport_uk.transport_uk_destination, section.section_en, attached_corps.corps_en AS attached_corps_en, birth_date, birth_year, birth_country.country_en AS birth_country_en, mother_name, mother_origin.country_en AS mother_origin_en, father_name, father_origin.country_en AS father_origin_en, nz_resident_in_month, marital_status.marital_status_en, wife_name, occupation.occupation_en, religion.religion_en, enlistment_date, military_district_name, posted_date, posted_from_corps.corps_en AS posted_from_corps_en, awmm_cenotaph, nominal_roll.nominal_roll_volume, nominal_roll.nominal_roll_number, nominal_roll.nominal_roll_page, image

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
        LEFT JOIN religion ON t.religion_fk=religion.religion_id
        LEFT JOIN military_district ON t.military_district_fk=military_district.military_district_id
        LEFT JOIN corps posted_from_corps ON t.posted_corps_fk=posted_from_corps.corps_id
        LEFT JOIN nominal_roll ON t.nominal_roll_fk=nominal_roll.nominal_roll_id

        WHERE id=%s'''
    values = [id]
    tunneller_result = run_sql(tunneller_sql, mysql, values)

    nz_archives_sql = 'SELECT nz_archives_ref, nz_archives_url FROM nz_archives LEFT JOIN tunneller ON tunneller.id=nz_archives.nz_archives_t_id WHERE tunneller.id=%s'
    nz_archives_result = run_sql(nz_archives_sql, mysql, values)

    london_gazette_sql = 'SELECT london_gazette_date, london_gazette_page FROM london_gazette_join JOIN london_gazette ON london_gazette.london_gazette_id=london_gazette_join.london_gazette_lg_id WHERE london_gazette_join.london_gazette_t_id=%s'
    london_gazette_result = run_sql(london_gazette_sql, mysql, values)

    image_source_sql = f'''
        SELECT image_source_auckland_libraries, archives_name, archives_ref, family_name, newspaper_name, newspaper_date
        
        FROM image_source 
        
        LEFT JOIN tunneller ON tunneller.id=image_source.image_source_t_id
        LEFT JOIN archives ON archives.archives_id=image_source.image_source_archives_fk
        LEFT JOIN archives_name ON archives_name.archives_name_id=archives.archives_name_fk
        LEFT JOIN family ON family.family_id=image_source.image_source_family_fk
        LEFT JOIN newspaper ON newspaper.newspaper_id=image_source.image_source_newspaper_fk
        LEFT JOIN newspaper_name ON newspaper_name.newspaper_name_id=newspaper.newspaper_name_fk
        
        WHERE tunneller.id=%s'''
    image_source_result = run_sql(image_source_sql, mysql, values)

    return tunneller_result, nz_archives_result, london_gazette_result, image_source_result
