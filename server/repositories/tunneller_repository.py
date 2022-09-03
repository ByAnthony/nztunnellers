from db.run_sql import run_sql


def show(id, mysql):
    sql = f'''
        SELECT id, surname, forename, aka, serial, rank_fk, rank_en, birth_date, birth_country_fk, birth_country.country_en AS birth_country_en, mother_name, mother_origin_fk, mother_origin.country_en AS mother_origin_en, father_name, father_origin_fk, father_origin.country_en AS father_origin_en, marital_status.marital_status_en, religion.religion_en, nz_archives_ref_1, nz_archives_url_1, nz_archives_ref_2, nz_archives_url_2, awmm_cenotaph, nominal_roll_fk, nominal_roll.nominal_roll_volume, nominal_roll.nominal_roll_number, nominal_roll.nominal_roll_page

        FROM tunneller t

        LEFT JOIN rank ON t.rank_fk=rank.rank_id
        LEFT JOIN country birth_country ON t.birth_country_fk=birth_country.country_id
        LEFT JOIN country mother_origin ON t.mother_origin_fk=mother_origin.country_id
        LEFT JOIN country father_origin ON t.father_origin_fk=father_origin.country_id
        LEFT JOIN marital_status ON t.marital_status_fk=marital_status.marital_status_id
        LEFT JOIN religion ON t.religion_fk=religion.religion_id
        LEFT JOIN nominal_roll ON t.nominal_roll_fk=nominal_roll.nominal_roll_id

        WHERE id=%s

        ORDER BY surname, forename
    '''
    values = [id]
    result = run_sql(sql, mysql, values)
    return result
