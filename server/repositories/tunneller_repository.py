# -*- coding: utf-8 -*-
from typing import Optional
from dacite import from_dict
from flask_mysqldb import MySQL


from ..db.run_sql import run_sql
from .data.images_data import images
from .data.origins_data import origins
from .data.pre_war_years_data import pre_war_years
from .data.sources_data import sources
from .data.summary_data import summary
from ..repositories.data.military_years_data import military_years
from ..repositories.data.post_service_years_data import post_service_years
from ..repositories.queries.army_experience_query import army_experience_query
from ..repositories.queries.book_authors_query import book_authors_query
from .queries.events_query import company_events_query, front_events_query
from ..repositories.queries.london_gazette_query import london_gazette_query
from ..repositories.queries.medals_query import medals_query
from ..repositories.queries.nz_archives_query import nz_archives_query
from ..repositories.queries.tunneller_query import tunneller_query
from ..models.image import ImageBookAuthors
from ..models.military_years import Medal, SingleEvent
from ..models.pre_war_years import ArmyExperience
from ..models.sources import LondonGazette, NewZealandArchives
from ..models.tunneller import Tunneller


def show(id: int, lang: str, mysql: MySQL) -> Optional[Tunneller]:

    tunneller_sql: str = tunneller_query(lang)
    values = [id]
    tunneller_result: Tunneller = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = army_experience_query(lang)
    army_experience_result: list[ArmyExperience] = run_sql(
        army_experience_sql, mysql, values
    )

    company_events_sql = company_events_query()
    company_events_result: list[SingleEvent] = run_sql(company_events_sql, mysql, None)

    front_events_sql = front_events_query()
    front_events_result: list[SingleEvent] = run_sql(front_events_sql, mysql, values)

    medals_sql = medals_query(lang)
    medals_result: list[Medal] = run_sql(medals_sql, mysql, values)

    nz_archives_sql = nz_archives_query()
    nz_archives_result: list[NewZealandArchives] = run_sql(
        nz_archives_sql, mysql, values
    )

    london_gazette_sql = london_gazette_query()
    london_gazette_result: list[LondonGazette] = run_sql(
        london_gazette_sql, mysql, values
    )

    book_authors_sql = book_authors_query()
    book_authors_result: list[ImageBookAuthors] = run_sql(
        book_authors_sql, mysql, values
    )

    if tunneller_result:

        data = {
            "id": tunneller_result["id"],
            "summary": summary(tunneller_result),
            "origins": origins(tunneller_result, lang),
            "pre_war_years": pre_war_years(
                army_experience_result, tunneller_result, lang
            ),
            "military_years": military_years(
                tunneller_result,
                company_events_result,
                front_events_result,
                medals_result,
                lang,
            ),
            "post_service_years": post_service_years(tunneller_result, lang),
            "sources": sources(
                nz_archives_result, tunneller_result, london_gazette_result, lang
            ),
            "image": images(tunneller_result, book_authors_result, lang),
        }

        return from_dict(data_class=Tunneller, data=data)

    return None
