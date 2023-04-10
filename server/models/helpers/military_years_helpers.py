# -*- coding: utf-8 -*-
from typing import Optional

from ...models.tunneller import Tunneller

from .date_helpers import (
    calculate_age_with_full_date,
    calculate_age_with_years,
    get_optional_date,
    get_full_date,
)
from ..date import Date
from ..death import Cemetery, Death, DeathCause, DeathPlace
from .translator_helpers import (
    translate_superscript,
    translate_transport_ref,
)
from ..military_years import (
    Demobilization,
    EventDetails,
    Events,
    Medal,
    SingleEvent,
    Training,
    Transferred,
    TransferredToTunnellers,
    Transport,
)


def get_training(
    date: Optional[Date],
    location: str,
    location_type: str,
) -> Optional[Training]:
    if date is not None:
        return Training(date, location, location_type)
    return None


def get_transferred_to_tunnellers(
    date: Optional[Date], posted_from: Optional[str]
) -> Optional[TransferredToTunnellers]:
    if date is not None and posted_from is not None:
        return TransferredToTunnellers(date, posted_from)
    return None


def get_detachment(detachment: str, lang: str) -> Optional[str]:
    return translate_superscript(detachment, lang)


def get_section(section: Optional[str], lang: str) -> Optional[str]:
    if section is not None:
        return translate_superscript(section, lang)
    return None


def get_transport_reference(transport_reference: str, lang: str) -> str:
    return translate_transport_ref(transport_reference, lang)


def get_transport_nz(
    transport_reference: str,
    vessel: str,
    departure_date: Optional[Date],
    departure_port: Optional[str],
    arrival_date: Optional[Date],
    arrival_port: Optional[str],
) -> Optional[Transport]:
    if transport_reference and vessel and departure_date is not None:
        return Transport(
            transport_reference,
            vessel,
            departure_date,
            departure_port,
            arrival_date,
            arrival_port,
        )
    return None


def get_boolean(data: Optional[int]) -> bool:
    if data == 1:
        return True
    return False


def get_transferred_to(
    date: Optional[str], unit: Optional[str], lang: str
) -> Optional[Transferred]:
    formatted_date = get_optional_date(date, lang)
    formatted_unit = translate_superscript(unit, lang)
    if formatted_date is not None and formatted_unit is not None:
        return Transferred(formatted_date, formatted_unit)
    return None


def get_death_war(
    death_type: Optional[str],
    date: Optional[Date],
    place: Optional[DeathPlace],
    cause: Optional[DeathCause],
    cemetery: Optional[Cemetery],
    age_at_death: Optional[int],
) -> Optional[Death]:
    if death_type == "War":
        return Death(date, place, cause, cemetery, age_at_death)
    return None


def get_death_place(
    location: Optional[str], town: Optional[str], country: Optional[str]
) -> Optional[DeathPlace]:
    if location is None and town is None and country is None:
        return None
    return DeathPlace(location, town, country)


def get_death_circumstances(
    cause: Optional[str], circumstances: Optional[str]
) -> Optional[DeathCause]:
    if cause is not None and circumstances is not None:
        return DeathCause(cause, circumstances)
    elif cause is not None and circumstances is None:
        return DeathCause(cause, None)
    return None


def get_cemetery(
    name: Optional[str], location: str, country: str, grave: Optional[str]
) -> Optional[Cemetery]:
    if name is not None:
        return Cemetery(name, location, country, grave)
    return None


def get_age(
    year_1: Optional[str],
    date_1: Optional[str],
    year_2: Optional[str],
    date_2: Optional[str],
) -> Optional[int]:
    if (
        date_1 is not None
        and year_1 is not None
        and date_2 is not None
        and year_2 is not None
    ):
        return calculate_age_with_full_date(date_2, date_1)
    if year_1 is not None and date_1 is None and year_2 is not None and date_2 is None:
        return calculate_age_with_years(year_2, year_1)
    if (
        year_2 is not None
        and date_2 is None
        and year_1 is not None
        and date_1 is not None
    ):
        return calculate_age_with_years(year_2, year_1)
    if (
        year_1 is not None
        and date_1 is None
        and year_2 is not None
        and date_2 is not None
    ):
        return calculate_age_with_years(year_2, year_1)
    return None


def get_end_of_service(date: Optional[Date], country: str) -> Optional[Demobilization]:
    if date is not None:
        return Demobilization(date, country)
    return None


def get_end_of_service_country(discharge_uk: Optional[int], lang: str) -> str:
    if get_boolean(discharge_uk) is True:
        if lang == "en":
            return "United Kingdom"
        return "Royaume-Uni"
    else:
        if lang == "en":
            return "New Zealand"
        return "Nouvelle-Zélande"


def map_front_events(
    company_events: list[SingleEvent],
    tunneller_events: list[SingleEvent],
    tunneller: Tunneller,
    lang: str,
) -> list[Events]:
    def create_event(date: Date, event: str, title: Optional[str]) -> SingleEvent:
        return SingleEvent(date, EventDetails(event, title))

    event_start_date = min(event["date"] for event in tunneller_events)
    event_end_date = max(event["date"] for event in tunneller_events)

    selected_events: list[SingleEvent] = []
    for event in company_events:
        if (
            event["event"] != "Marched in to the Company Training Camp, Falmouth"
            and event_start_date <= event["date"] <= event_end_date
        ):
            selected_events.append(event)
        if (
            event["event"] == "Marched in to the Company Training Camp, Falmouth"
            and tunneller["transport_uk_ref"] == "S.S. Ruapehu 18 December 1915"
        ):
            selected_events.append(event)

    if tunneller["transport_uk_start"] is not None:
        vessel_to_england = "{} {}".format(
            tunneller["transport_uk_ref"], tunneller["transport_uk_vessel"]
        )
        selected_events.append(
            create_event(
                tunneller["transport_uk_start"],
                vessel_to_england,
                "Transfer to England",
            )
        )

    selected_and_tunneller_events = sorted(
        list(selected_events + list(tunneller_events)), key=lambda item: item["date"]
    )

    result: list[SingleEvent] = []
    for event in selected_and_tunneller_events:
        mapped_event = SingleEvent(
            get_full_date(event["date"], lang),
            EventDetails(event["event"], event["title"]),
        )
        result.append(mapped_event)

    events_grouped_by_date: list[Events] = []
    for event in result:
        event_date = event["date"]
        event_description = event["event"]
        for grp_event in events_grouped_by_date:
            if grp_event["date"] == event_date:
                grp_event["event"].append(event_description)
                break
        else:
            events_grouped_by_date.append(Events(event_date, [event_description]))
    return events_grouped_by_date


def map_medals(medals: list[Medal]) -> list[Medal]:
    return [
        Medal(medal["name"], medal["country"], medal["citation"]) for medal in medals
    ]
