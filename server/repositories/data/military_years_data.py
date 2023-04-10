# -*- coding: utf-8 -*-
from typing import Optional

from ...models.death import Death
from ...models.helpers.translator_helpers import translate_town
from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    get_optional_date,
)
from ...models.helpers.military_years_helpers import (
    get_age,
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
    map_front_events,
)
from ...models.military_years import (
    Demobilization,
    EmbarkationUnit,
    EndOfService,
    Enlistment,
    Medal,
    MilitaryYears,
    SingleEvent,
    Transferred,
    Transport,
)
from ...models.tunneller import Tunneller


def enlistment(tunneller: Tunneller, lang: str) -> Enlistment:
    return Enlistment(
        tunneller["serial"],
        tunneller["rank"],
        get_optional_date(tunneller["enlistment_date"], lang),
        tunneller["military_district_name"],
        tunneller["aka"],
        get_transferred_to_tunnellers(
            get_optional_date(tunneller["posted_date"], lang),
            tunneller["posted_from_corps"],
        ),
    )


def embarkation_unit(tunneller: Tunneller, lang: str) -> EmbarkationUnit:
    return EmbarkationUnit(
        get_detachment(tunneller["embarkation_unit"], lang),
        get_training(
            get_optional_date(tunneller["training_start"], lang),
            tunneller["training_location"],
            tunneller["training_location_type"],
        ),
        get_section(tunneller["section"], lang),
        tunneller["attached_corps"],
    )


def transferred(tunneller: Tunneller, lang: str) -> Optional[Transferred]:
    return get_transferred_to(
        tunneller["transferred_to_date"],
        tunneller["transferred_to_unit"],
        lang,
    )


def death_war(tunneller: Tunneller, lang: str) -> Optional[Death]:
    return get_death_war(
        tunneller["death_type"],
        format_birth_and_death_date(
            tunneller["death_year"],
            tunneller["death_date"],
            lang,
        ),
        get_death_place(
            tunneller["death_location"],
            translate_town(tunneller["death_town"], lang),
            tunneller["death_country"],
        ),
        get_death_circumstances(
            tunneller["death_cause"],
            tunneller["death_circumstances"],
        ),
        get_cemetery(
            tunneller["cemetery"],
            tunneller["cemetery_town"],
            tunneller["cemetery_country"],
            tunneller["grave"],
        ),
        get_age(
            tunneller["death_year"],
            tunneller["death_date"],
            tunneller["birth_year"],
            tunneller["birth_date"],
        ),
    )


def demobilization(tunneller: Tunneller, lang: str) -> Optional[Demobilization]:
    return get_end_of_service(
        get_optional_date(tunneller["demobilization_date"], lang),
        get_end_of_service_country(tunneller["discharge_uk"], lang),
    )


def end_of_service(tunneller: Tunneller, lang: str) -> EndOfService:
    return EndOfService(
        get_boolean(tunneller["has_deserted"]),
        transferred(tunneller, lang),
        death_war(tunneller, lang),
        get_transport_nz(
            get_transport_reference(tunneller["transport_nz_ref"], lang),
            tunneller["transport_nz_vessel"],
            get_optional_date(tunneller["transport_nz_start"], lang),
            tunneller["transport_nz_origin"],
            get_optional_date(tunneller["transport_nz_end"], lang),
            tunneller["transport_nz_destination"],
        ),
        demobilization(tunneller, lang),
    )


def military_years(
    tunneller: Tunneller,
    company_events: list[SingleEvent],
    tunneller_events: list[SingleEvent],
    medals: list[Medal],
    lang: str,
) -> MilitaryYears:
    return MilitaryYears(
        enlistment(tunneller, lang),
        embarkation_unit(tunneller, lang),
        Transport(
            get_transport_reference(tunneller["transport_uk_ref"], lang),
            tunneller["transport_uk_vessel"],
            get_optional_date(tunneller["transport_uk_start"], lang),
            tunneller["transport_uk_origin"],
            get_optional_date(tunneller["transport_uk_end"], lang),
            tunneller["transport_uk_destination"],
        ),
        map_front_events(company_events, tunneller_events, tunneller, lang),
        end_of_service(tunneller, lang),
        map_medals(medals),
    )
