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
from .data.sources_data import sources
from ..models.death import Cemetery, DeathCause, DeathPlace
from ..models.helpers.date_helpers import (
    format_date_string_to_date_type,
    format_date_to_day_month_and_year,
    format_date_to_year,
    get_optional_date,
)
from ..models.helpers.image_helpers import (
    get_image_source_archives,
    get_image_source_book,
    get_image_source_newspaper,
)
from ..models.helpers.military_years_helpers import (
    get_age,
    get_boolean,
    get_cemetery,
    get_death_circumstances,
    get_death_place,
    get_detachment,
    get_section,
    get_training,
    get_transferred_to_tunnellers,
    get_transport_reference,
    map_front_events,
    map_medals,
)
from ..models.helpers.origins_helpers import get_nz_resident, get_parent
from ..models.helpers.post_service_years_helpers import get_death
from ..models.helpers.pre_war_years_helpers import map_army_experience
from ..models.helpers.sources_helpers import get_nominal_roll
from ..models.helpers.translator_helpers import translate_town
from ..models.image import ImageArchives, ImageBook, ImageNewspaper
from ..models.military_years import (
    EmbarkationUnit,
    EndOfService,
    Enlistment,
    MilitaryYears,
    Transport,
)
from ..models.origins import BirthDetails, Origins, Parents
from ..models.post_service_years import PostServiceYears
from ..models.pre_war_years import Employment, PreWarYear
from ..models.roll import Name
from ..models.sources import NominalRoll
from ..models.summary import Summary
from ..models.tunneller import Tunneller
from ..repositories.data.military_years_data import (
    death_war,
    demobilization,
    get_age_at_enlistment,
    transferred,
)
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

        summary = Summary(
            Name(
                tunneller_result["forename"],
                tunneller_result["surname"],
            ),
            format_date_to_year(tunneller_result["birth_date"]),
            format_date_to_year(tunneller_result["death_date"]),
        )

        origins = Origins(
            BirthDetails(
                format_date_string_to_date_type(
                    format_date_to_year(tunneller_result["birth_date"]),
                    tunneller_result["birth_date"],
                    lang,
                ),
                tunneller_result["birth_country"],
            ),
            Parents(
                get_parent(
                    tunneller_result["mother_name"],
                    tunneller_result["mother_origin"],
                ),
                get_parent(
                    tunneller_result["father_name"],
                    tunneller_result["father_origin"],
                ),
            ),
            get_nz_resident(
                tunneller_result["nz_resident_in_month"],
                tunneller_result["enlistment_date"],
            ),
        )

        pre_war = PreWarYear(
            map_army_experience(army_experience_result, lang),
            Employment(tunneller_result["occupation"], tunneller_result["employer"]),
            tunneller_result["residence"],
            tunneller_result["marital_status"],
            tunneller_result["wife_name"],
            tunneller_result["religion"],
        )

        military_years = MilitaryYears(
            Enlistment(
                tunneller_result["serial"],
                tunneller_result["rank"],
                get_optional_date(tunneller_result["enlistment_date"], lang),
                tunneller_result["military_district_name"],
                tunneller_result["aka"],
                get_transferred_to_tunnellers(
                    get_optional_date(tunneller_result["posted_date"], lang),
                    tunneller_result["posted_from_corps"],
                ),
                get_age_at_enlistment(
                    tunneller_result["enlistment_date"],
                    tunneller_result["posted_date"],
                    tunneller_result,
                ),
            ),
            EmbarkationUnit(
                get_detachment(tunneller_result["embarkation_unit"], lang),
                get_training(
                    get_optional_date(tunneller_result["training_start"], lang),
                    tunneller_result["training_location"],
                    tunneller_result["training_location_type"],
                ),
                get_section(tunneller_result["section"], lang),
                tunneller_result["attached_corps"],
            ),
            Transport(
                get_transport_reference(tunneller_result["transport_uk_ref"], lang),
                tunneller_result["transport_uk_vessel"],
                get_optional_date(tunneller_result["transport_uk_start"], lang),
                tunneller_result["transport_uk_origin"],
                get_optional_date(tunneller_result["transport_uk_end"], lang),
                tunneller_result["transport_uk_destination"],
            ),
            map_front_events(
                company_events_result, front_events_result, tunneller_result, lang
            ),
            EndOfService(
                get_boolean(tunneller_result["has_deserted"]),
                transferred(tunneller_result, lang),
                death_war(tunneller_result, lang),
                Transport(
                    get_transport_reference(tunneller_result["transport_nz_ref"], lang),
                    tunneller_result["transport_nz_vessel"],
                    get_optional_date(tunneller_result["transport_nz_start"], lang),
                    tunneller_result["transport_nz_origin"],
                    get_optional_date(tunneller_result["transport_nz_end"], lang),
                    tunneller_result["transport_nz_destination"],
                ),
                demobilization(tunneller_result, lang),
            ),
            map_medals(medals_result),
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

        image_source_archives: Optional[ImageArchives] = get_image_source_archives(
            tunneller_result["archives_name"],
            tunneller_result["archives_ref"],
        )

        image_source_newspaper: Optional[ImageNewspaper] = get_image_source_newspaper(
            tunneller_result["newspaper_name"],
            format_date_to_day_month_and_year(tunneller_result["newspaper_date"], lang),
        )

        image_source_book: Optional[ImageBook] = get_image_source_book(
            book_authors_result,
            tunneller_result["book_title"],
            tunneller_result["book_town"],
            tunneller_result["book_publisher"],
            tunneller_result["book_year"],
            tunneller_result["book_page"],
        )

        data = {
            "id": tunneller_result["id"],
            "summary": summary,
            "origins": origins,
            "pre_war_years": pre_war,
            "military_years": military_years,
            "post_service_years": PostServiceYears(
                get_death(
                    tunneller_result["death_type"],
                    format_date_string_to_date_type(
                        format_date_to_year(tunneller_result["death_date"]),
                        tunneller_result["death_date"],
                        lang,
                    ),
                    death_place,
                    death_circumstances,
                    cemetery,
                    age_at_death,
                )
            ),
            "sources": sources(
                nz_archives_result,
                tunneller_result["awmm_cenotaph"],
                nominal_roll,
                london_gazette_result,
                lang,
            ),
            "image": images(
                tunneller_result["image"],
                tunneller_result["image_source_auckland_libraries"],
                image_source_archives,
                tunneller_result["family_name"],
                image_source_newspaper,
                image_source_book,
                lang,
            ),
        }

        return from_dict(data_class=Tunneller, data=data)

    return None
