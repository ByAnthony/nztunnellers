# -*- coding: utf-8 -*-
from ...repositories.translations.translations import (
    conflict_col,
    country_col,
)


def army_experience_query(lang: str) -> str:
    return f"""SELECT
        army_experience.army_experience_name AS unit
        , {country_col[lang]} AS country
        , {conflict_col[lang]} AS conflict
        , CONVERT(army_experience_join.army_experience_in_month, char) AS duration

        FROM army_experience

        LEFT JOIN army_experience_join ON army_experience_join.army_experience_c_id=army_experience.army_experience_id
        LEFT JOIN country ON country.country_id=army_experience_join.army_experience_c_c_id
        LEFT JOIN conflict ON conflict.conflict_id=army_experience_join.army_experience_w_id

        WHERE army_experience_join.army_experience_t_id=%s"""
