# -*- coding: utf-8 -*-
from typing import Optional
from dacite import from_dict
from ..repositories.queries.tunneller_query import tunneller_query
from ..repositories.queries.army_experience_query import army_experience_query
from ..repositories.queries.medals_query import medals_query
from ..repositories.queries.nz_archives_query import nz_archives_query
from ..repositories.queries.london_gazette_query import london_gazette_query
from ..repositories.queries.book_authors_query import book_authors_query
from ..models.helpers.name_helpers import set_surname_to_uppercase
from ..models.helpers.post_service_years_helpers import get_death
from ..models.helpers.translator_helpers import translate_town
from ..db.run_sql import run_sql
from flask_mysqldb import MySQL
from ..models.helpers.date_helpers import (
    format_date_to_birth_year,
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
            "summary": {
                "name": {
                    "forename": tunneller_result["forename"],
                    "surname": set_surname_to_uppercase(tunneller_result["surname"]),
                },
                "birth": format_date_to_birth_year(
                    tunneller_result["birth_year"],
                    tunneller_result["birth_date"],
                ),
                "death": format_date_to_birth_year(
                    tunneller_result["death_year"],
                    tunneller_result["death_date"],
                ),
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
                "inNzLength": get_nz_resident(
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

    return None
