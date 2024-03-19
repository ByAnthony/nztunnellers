# -*- coding: utf-8 -*-
from typing import Optional

# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL  # type: ignore
from dacite import from_dict


from ..db.models.TunnellerData import (
    ArmyExperienceData,
    BookAuthorsData,
    LondonGazetteData,
    MedalData,
    NewZealandArchivesData,
    SingleEventData,
    TunnellerData,
)
from ..db.run_sql import run_sql
from .data.images_data import images
from .data.origins_data import origins
from .data.pre_war_years_data import pre_war_years
from .data.sources_data import sources
from .data.summary_data import summary
from ..models.death import Cemetery, DeathCause, DeathPlace
from ..models.helpers.date_helpers import format_date_to_year
from ..models.helpers.military_years_helpers import (
    get_age,
    get_cemetery,
    get_death_circumstances,
    get_death_place,
)
from ..models.helpers.origins_helpers import get_nz_resident, get_parent
from ..models.helpers.sources_helpers import get_nominal_roll
from ..models.helpers.translator_helpers import translate_town
from ..models.origins import Parents
from ..models.pre_war_years import Employment
from ..models.sources import NominalRoll
from ..models.tunneller import Tunneller
from ..repositories.data.military_years_data import military_years
from ..repositories.data.post_service_years_data import post_service_years
from ..repositories.queries.army_experience_query import army_experience_query
from ..repositories.queries.book_authors_query import book_authors_query
from .queries.events_query import company_events_query, front_events_query
from ..repositories.queries.london_gazette_query import london_gazette_query
from ..repositories.queries.medals_query import medals_query
from ..repositories.queries.nz_archives_query import nz_archives_query
from ..repositories.queries.tunneller_query import tunneller_query


def show(id: int, lang: str, mysql: MySQL) -> Optional[Tunneller]:

    tunneller_sql: str = tunneller_query(lang)
    values: list[int] = [id]
    tunneller_result: TunnellerData = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = army_experience_query(lang)
    army_experience_result: tuple[ArmyExperienceData] = run_sql(
        army_experience_sql, mysql, values
    )

    company_events_sql = company_events_query()
    company_events_result: tuple[SingleEventData] = run_sql(
        company_events_sql, mysql, None
    )

    front_events_sql = front_events_query()
    front_events_result: tuple[SingleEventData] = run_sql(
        front_events_sql, mysql, values
    )

    medals_sql = medals_query(lang)
    medals_result: tuple[MedalData] = run_sql(medals_sql, mysql, values)

    nz_archives_sql = nz_archives_query()
    nz_archives_result: tuple[NewZealandArchivesData] = run_sql(
        nz_archives_sql, mysql, values
    )

    london_gazette_sql = london_gazette_query()
    london_gazette_result: tuple[LondonGazetteData] = run_sql(
        london_gazette_sql, mysql, values
    )

    book_authors_sql = book_authors_query()
    book_authors_result: tuple[BookAuthorsData] = run_sql(
        book_authors_sql, mysql, values
    )

    if tunneller_result:

        parents: Parents = Parents(
            get_parent(
                tunneller_result["mother_name"],
                tunneller_result["mother_origin"],
            ),
            get_parent(
                tunneller_result["father_name"],
                tunneller_result["father_origin"],
            ),
        )

        nz_resident: Optional[str] = get_nz_resident(
            tunneller_result["nz_resident_in_month"],
            tunneller_result["enlistment_date"],
        )

        employment: Employment = Employment(
            tunneller_result["occupation"], tunneller_result["employer"]
        )

        death_place: Optional[DeathPlace] = get_death_place(
            tunneller_result["death_location"],
            translate_town(tunneller_result["death_town"], lang),
            tunneller_result["death_country"],
        )

        death_circumstances: Optional[DeathCause] = get_death_circumstances(
            tunneller_result["death_cause"],
            tunneller_result["death_circumstances"],
        )

        cemetery: Optional[Cemetery] = get_cemetery(
            tunneller_result["cemetery"],
            tunneller_result["cemetery_town"],
            tunneller_result["cemetery_country"],
            tunneller_result["grave"],
        )

        age_at_death: Optional[int] = get_age(
            format_date_to_year(tunneller_result["death_date"]),
            tunneller_result["death_date"],
            format_date_to_year(tunneller_result["birth_date"]),
            tunneller_result["birth_date"],
        )

        nominal_roll: NominalRoll = get_nominal_roll(
            tunneller_result["nominal_roll_volume"],
            tunneller_result["nominal_roll_number"],
            tunneller_result["nominal_roll_page"],
            lang,
        )

        data = {
            "id": tunneller_result["id"],
            "summary": summary(
                tunneller_result["forename"],
                tunneller_result["surname"],
                tunneller_result["birth_date"],
                tunneller_result["death_date"],
            ),
            "origins": origins(
                tunneller_result["birth_date"],
                tunneller_result["birth_country"],
                parents,
                nz_resident,
                lang,
            ),
            "pre_war_years": pre_war_years(
                army_experience_result,
                employment,
                tunneller_result["residence"],
                tunneller_result["marital_status"],
                tunneller_result["wife_name"],
                tunneller_result["religion"],
                lang,
            ),
            "military_years": military_years(
                tunneller_result,
                company_events_result,
                front_events_result,
                medals_result,
                lang,
            ),
            "post_service_years": post_service_years(
                tunneller_result["death_type"],
                tunneller_result["death_date"],
                death_place,
                death_circumstances,
                cemetery,
                age_at_death,
                lang,
            ),
            "sources": sources(
                nz_archives_result,
                tunneller_result["awmm_cenotaph"],
                nominal_roll,
                london_gazette_result,
                lang,
            ),
            "image": images(tunneller_result, book_authors_result, lang),
        }

        return from_dict(data_class=Tunneller, data=data)

    return None
