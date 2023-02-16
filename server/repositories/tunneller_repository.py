# -*- coding: utf-8 -*-
from typing import Optional
from dacite import from_dict
from ..repositories.data.images import images
from ..repositories.data.sources import sources
from ..repositories.data.pre_war_years import pre_war_years
from ..repositories.data.origins import origins
from ..repositories.data.summary import summary
from ..repositories.queries.tunneller_query import tunneller_query
from ..repositories.queries.army_experience_query import army_experience_query
from ..repositories.queries.medals_query import medals_query
from ..repositories.queries.nz_archives_query import nz_archives_query
from ..repositories.queries.london_gazette_query import london_gazette_query
from ..repositories.queries.book_authors_query import book_authors_query
from ..models.helpers.post_service_years_helpers import get_death
from ..models.helpers.translator_helpers import translate_town
from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.helpers.date_helpers import (
    get_birth_date,
    get_date,
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
from ..models.image import ImageBookAuthors
from ..models.military_years import Medal
from ..models.pre_war_years import ArmyExperience
from ..models.sources import LondonGazette, NewZealandArchives
from ..models.tunneller import Tunneller


def show(id: int, lang: str, mysql: MySQL) -> Optional[Tunneller]:

    tunneller_sql = tunneller_query(lang)
    values = [id]
    tunneller_result: Tunneller = run_sql(tunneller_sql, mysql, values)[0]

    army_experience_sql = army_experience_query(lang)
    army_experience_result: list[ArmyExperience] = run_sql(
        army_experience_sql, mysql, values
    )

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
            "military_years": {
                "enlistment": {
                    "serial": tunneller_result["serial"],
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
            "post_service_years": {
                "death": get_death(
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
            },
            "sources": sources(
                nz_archives_result, tunneller_result, london_gazette_result, lang
            ),
            "image": images(tunneller_result, book_authors_result, lang),
        }

        tunneller: Tunneller = from_dict(data_class=Tunneller, data=data)

        return tunneller

    return None
