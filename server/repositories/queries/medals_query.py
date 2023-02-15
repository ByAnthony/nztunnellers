# -*- coding: utf-8 -*-
from ...repositories.translations.translations import (
    medal_name_col,
    country_col,
    medal_citation_col,
)


def medals_query(lang: str) -> str:
    return f"""SELECT
        {medal_name_col[lang]} AS name
        , {country_col[lang]} AS country
        , {medal_citation_col[lang]} AS citation

        FROM medal

        JOIN medal_join ON medal_join.medal_m_id=medal.medal_id
        LEFT JOIN medal_citation ON medal_citation.medal_citation_id=medal_c_id
        LEFT JOIN country ON country.country_id=medal_m_c_id

        WHERE medal_join.medal_t_id=%s"""
