from db.run_sql import run_sql


def show(id, mysql):
    tunneller_sql = f'''
        SELECT id, surname, forename, aka, serial, rank_fk, rank_en, embarkation_unit.embarkation_unit_en, training.training_start, training.training_location, training_location_type.training_location_type_en, transport_uk.transport_uk_ref, transport_uk.transport_uk_vessel, transport_uk.transport_uk_start, transport_uk.transport_uk_origin, transport_uk.transport_uk_end, transport_uk.transport_uk_destination, section.section_en, attached_corps.corps_en AS attached_corps_en, birth_date, birth_country.country_en AS birth_country_en, mother_name, mother_origin.country_en AS mother_origin_en, father_name, father_origin.country_en AS father_origin_en, nz_resident_in_month, marital_status.marital_status_en, wife_name, occupation.occupation_en, religion.religion_en, enlistment_date, military_district_name, posted_date, posted_from_corps.corps_en AS posted_from_corps_en, nz_archives_ref_1, nz_archives_url_1, nz_archives_ref_2, nz_archives_url_2, awmm_cenotaph, nominal_roll.nominal_roll_volume, nominal_roll.nominal_roll_number, nominal_roll.nominal_roll_page 

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

        WHERE id=%s

        ORDER BY surname, forename
    '''
    values = [id]
    tunneller_result = run_sql(tunneller_sql, mysql, values)

    london_gazette_sql = 'SELECT london_gazette_date, london_gazette_page FROM london_gazette_join JOIN london_gazette ON london_gazette.london_gazette_id=london_gazette_join.london_gazette_lg_id WHERE london_gazette_join.london_gazette_t_id=%s'
    london_gazette_result = run_sql(london_gazette_sql, mysql, values)

    return tunneller_result, london_gazette_result
