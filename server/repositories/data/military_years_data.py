# -*- coding: utf-8 -*-
from typing import Optional

from ...models.death import Death
from ...models.helpers.translator_helpers import translate_town
from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    get_optional_date,
)
from ...models.helpers.military_years_helpers import (
    get_age_at_death,
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
    map_wwi_events,
)
from ...models.military_years import (
    Demobilization,
    EmbarkationUnit,
    EndOfService,
    Enlistment,
    Event,
    Medal,
    MilitaryYears,
    Transferred,
    Transport,
)
from ...models.tunneller import Tunneller


def enlistment(tunneller_result: Tunneller, lang: str) -> Enlistment:
    return Enlistment(
        tunneller_result["serial"],
        tunneller_result["rank"],
        get_optional_date(tunneller_result["enlistment_date"], lang),
        tunneller_result["military_district_name"],
        tunneller_result["aka"],
        get_transferred_to_tunnellers(
            get_optional_date(tunneller_result["posted_date"], lang),
            tunneller_result["posted_from_corps"],
        ),
    )


def embarkation_unit(tunneller_result: Tunneller, lang: str) -> EmbarkationUnit:
    return EmbarkationUnit(
        get_detachment(tunneller_result["embarkation_unit"], lang),
        get_training(
            get_optional_date(tunneller_result["training_start"], lang),
            tunneller_result["training_location"],
            tunneller_result["training_location_type"],
        ),
        get_section(tunneller_result["section"], lang),
        tunneller_result["attached_corps"],
    )


def transferred(tunneller_result: Tunneller, lang: str) -> Optional[Transferred]:
    return get_transferred_to(
        tunneller_result["transferred_to_date"],
        tunneller_result["transferred_to_unit"],
        lang,
    )


def death_war(tunneller_result: Tunneller, lang: str) -> Optional[Death]:
    return get_death_war(
        tunneller_result["death_type"],
        format_birth_and_death_date(
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
        get_age_at_death(
            tunneller_result["death_year"],
            tunneller_result["death_date"],
            tunneller_result["birth_year"],
            tunneller_result["birth_date"],
        ),
    )


def demobilization(tunneller_result: Tunneller, lang: str) -> Optional[Demobilization]:
    return get_end_of_service(
        get_optional_date(tunneller_result["demobilization_date"], lang),
        get_end_of_service_country(tunneller_result["discharge_uk"], lang),
    )


def end_of_service(tunneller_result: Tunneller, lang: str) -> EndOfService:
    return EndOfService(
        get_boolean(tunneller_result["has_deserted"]),
        transferred(tunneller_result, lang),
        death_war(tunneller_result, lang),
        get_transport_nz(
            get_transport_reference(tunneller_result["transport_nz_ref"], lang),
            tunneller_result["transport_nz_vessel"],
            get_optional_date(tunneller_result["transport_nz_start"], lang),
            tunneller_result["transport_nz_origin"],
            get_optional_date(tunneller_result["transport_nz_end"], lang),
            tunneller_result["transport_nz_destination"],
        ),
        demobilization(tunneller_result, lang),
    )


def military_years(
    tunneller_result: Tunneller,
    wwi_events_result: list[Event],
    medals_result: list[Medal],
    lang: str,
) -> MilitaryYears:
    return MilitaryYears(
        enlistment(tunneller_result, lang),
        embarkation_unit(tunneller_result, lang),
        Transport(
            get_transport_reference(tunneller_result["transport_uk_ref"], lang),
            tunneller_result["transport_uk_vessel"],
            get_optional_date(tunneller_result["transport_uk_start"], lang),
            tunneller_result["transport_uk_origin"],
            get_optional_date(tunneller_result["transport_uk_end"], lang),
            tunneller_result["transport_uk_destination"],
        ),
        map_wwi_events(wwi_events_result, tunneller_result, lang),
        end_of_service(tunneller_result, lang),
        map_medals(medals_result),
    )
