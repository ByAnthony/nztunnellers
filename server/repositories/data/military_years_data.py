# -*- coding: utf-8 -*-
from typing import Optional

from ...db.models.TunnellerData import MedalData, SingleEventData, TunnellerData
from ...models.death import Death
from ...models.helpers.translator_helpers import translate_town
from ...models.helpers.date_helpers import (
    format_birth_and_death_date,
    format_date_to_year,
    get_optional_date,
)
from ...models.helpers.military_years_helpers import (
    get_age,
    get_cemetery,
    get_death_circumstances,
    get_death_place,
    get_death_war,
    get_end_of_service,
    get_end_of_service_country,
    get_transferred_to,
    map_medals,
    map_front_events,
)
from ...models.military_years import (
    Demobilization,
    EmbarkationUnit,
    EndOfService,
    Enlistment,
    MilitaryYears,
    Transferred,
    Transport,
)


def get_age_at_enlistment(
    enlistment_date: str, posted_date: str, tunneller: TunnellerData
) -> Optional[int]:
    if enlistment_date:
        return get_age(
            format_date_to_year(enlistment_date),
            enlistment_date,
            format_date_to_year(tunneller["birth_date"]),
            tunneller["birth_date"],
        )
    if posted_date:
        return get_age(
            format_date_to_year(posted_date),
            enlistment_date,
            format_date_to_year(tunneller["birth_date"]),
            tunneller["birth_date"],
        )
    return None


def transferred(tunneller: TunnellerData, lang: str) -> Optional[Transferred]:
    return get_transferred_to(
        tunneller["transferred_to_date"],
        tunneller["transferred_to_unit"],
        lang,
    )


def death_war(tunneller: TunnellerData, lang: str) -> Optional[Death]:
    return get_death_war(
        tunneller["death_type"],
        format_birth_and_death_date(
            format_date_to_year(tunneller["death_date"]),
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
            format_date_to_year(tunneller["death_date"]),
            tunneller["death_date"],
            format_date_to_year(tunneller["birth_date"]),
            tunneller["birth_date"],
        ),
    )


def demobilization(tunneller: TunnellerData, lang: str) -> Optional[Demobilization]:
    return get_end_of_service(
        get_optional_date(tunneller["demobilization_date"], lang),
        get_end_of_service_country(tunneller["discharge_uk"], lang),
    )


def military_years(
    enlistment: Enlistment,
    embarkation_unit: EmbarkationUnit,
    transport: Transport,
    end_of_service: EndOfService,
    tunneller: TunnellerData,
    company_events: tuple[SingleEventData],
    tunneller_events: tuple[SingleEventData],
    medals: tuple[MedalData],
    lang: str,
) -> MilitaryYears:
    return MilitaryYears(
        enlistment,
        embarkation_unit,
        transport,
        map_front_events(company_events, tunneller_events, tunneller, lang),
        end_of_service,
        map_medals(medals),
    )
