# -*- coding: utf-8 -*-
from typing import Optional

from ...db.models.TunnellerData import (
    DeathData,
    EndOfServiceData,
    EnlistmentData,
    MedalData,
    MilitaryYearsTunnellerData,
    PostedData,
    SingleEventData,
    Transport,
    TunnellerData,
)
from .date_helpers import (
    calculate_age_with_full_date,
    calculate_age_with_years,
    format_date_to_year,
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
    Event,
    EventDetails,
    Events,
    Medal,
    Training,
    Transferred,
    TransferredToTunnellers,
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


def get_age_at_enlistment(
    enlistment_date: str, posted_date: str, tunneller: TunnellerData
) -> Optional[int]:
    if enlistment_date:
        return get_age_at_death(
            format_date_to_year(enlistment_date),
            enlistment_date,
            format_date_to_year(tunneller["birth_date"]),
            tunneller["birth_date"],
        )
    if posted_date:
        return get_age_at_death(
            format_date_to_year(posted_date),
            enlistment_date,
            format_date_to_year(tunneller["birth_date"]),
            tunneller["birth_date"],
        )
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


def get_age_at_death(
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


def add_transports(
    transport_to_uk: Transport, transport_to_nz: Transport
) -> list[SingleEventData]:
    transports: list[SingleEventData] = []

    if transport_to_uk["date"] is not None:
        transports.append(
            SingleEventData(
                transport_to_uk["date"],
                f"{transport_to_uk['ref']} {transport_to_uk['vessel']}",
                transport_to_uk["title"],
                None,
            )
        )

    if transport_to_nz["date"] is not None:
        transports.append(
            SingleEventData(
                transport_to_nz["date"],
                f"{transport_to_nz['ref']} {transport_to_nz['vessel']}",
                transport_to_nz["title"],
                None,
            )
        )

    return transports


def add_end_of_service(endOfService: EndOfServiceData) -> list[SingleEventData]:
    end_of_service: list[SingleEventData] = []

    if endOfService["transferred_to_date"] is not None:
        end_of_service.append(
            SingleEventData(
                endOfService["transferred_to_date"],
                endOfService["transferred_to_unit"],
                "Transferred",
                None,
            )
        )
    if endOfService["demobilization_date"] is not None:
        if endOfService["discharge_uk"] == 1:
            end_of_service.append(
                SingleEventData(
                    endOfService["demobilization_date"],
                    "End of Service in the United Kingdom",
                    "Demobilization",
                    None,
                )
            )
        elif endOfService["has_deserted"] == 1:
            end_of_service.append(
                SingleEventData(
                    endOfService["demobilization_date"],
                    "End of Service as deserter",
                    "Demobilization",
                    None,
                )
            )
        else:
            end_of_service.append(
                SingleEventData(
                    endOfService["demobilization_date"],
                    "Demobilization",
                    "End of Service",
                    None,
                )
            )

    return end_of_service


def add_enlistment(enlistment: EnlistmentData) -> list[SingleEventData]:
    enlistment_event: list[SingleEventData] = []

    if enlistment["enlistment_date"] is not None:
        if enlistment["enlistment_date"] < enlistment["training_start"]:
            enlistment_event.append(
                SingleEventData(
                    enlistment["enlistment_date"],
                    enlistment["embarkation_unit"],
                    "Enlisted",
                    None,
                )
            )
            enlistment_event.append(
                SingleEventData(
                    enlistment["training_start"],
                    enlistment["training_location"],
                    "Trained",
                    None,
                )
            )
        else:
            enlistment_event.append(
                SingleEventData(
                    enlistment["enlistment_date"],
                    enlistment["embarkation_unit"],
                    "Enlisted",
                    None,
                )
            )
            enlistment_event.append(
                SingleEventData(
                    enlistment["enlistment_date"],
                    enlistment["training_location"],
                    "Trained",
                    None,
                )
            )

    return enlistment_event


def add_posted(posted: PostedData) -> list[SingleEventData]:
    posted_event: list[SingleEventData] = []

    if posted["posted_date"] is not None:
        if posted["posted_date"] < posted["training_start"]:
            posted_event.append(
                SingleEventData(
                    posted["posted_date"],
                    posted["embarkation_unit"],
                    "Posted",
                    None,
                )
            )
            posted_event.append(
                SingleEventData(
                    posted["training_start"],
                    posted["training_location"],
                    "Trained",
                    None,
                )
            )
        else:
            posted_event.append(
                SingleEventData(
                    posted["posted_date"],
                    posted["embarkation_unit"],
                    "Posted",
                    None,
                )
            )
            posted_event.append(
                SingleEventData(
                    posted["posted_date"],
                    posted["training_location"],
                    "Trained",
                    None,
                )
            )

    return posted_event


def add_death(death: DeathData) -> list[SingleEventData]:
    death_event: list[SingleEventData] = []

    if death["death_type"] == "War":
        if death["death_cause"] == "Killed in action":
            death_event.append(
                SingleEventData(
                    death["death_date"],
                    death["death_circumstances"],
                    death["death_cause"],
                    None,
                )
            )
        if death["death_cause"] == "Died of wounds":
            death_event.append(
                SingleEventData(
                    death["death_date"],
                    death["death_circumstances"],
                    death["death_cause"],
                    None,
                )
            )
        if death["death_cause"] == "Died of disease":
            death_event.append(
                SingleEventData(
                    death["death_date"],
                    f"{death['death_location']}, {death['death_town']}",
                    death["death_cause"],
                    None,
                )
            )
        if death["death_cause"] == "Died of accident":
            death_event.append(
                SingleEventData(
                    death["death_date"],
                    f"{death['death_location']}",
                    death["death_cause"],
                    None,
                )
            )
        death_event.append(
            SingleEventData(
                death["death_date"],
                f"{death['cemetery']}, {death['cemetery_town']}",
                "Buried",
                None,
            )
        )
        death_event.append(
            SingleEventData(
                death["death_date"], death["grave"], "Grave reference", None
            )
        )

    if death["death_type"] == "War injuries":
        if death["death_cause"] == "Died of disease":
            death_event.append(
                SingleEventData(
                    death["death_date"],
                    death["death_circumstances"],
                    death["death_cause"],
                    None,
                )
            )

    return death_event


def selected_company_events(
    main_tunneller_events: list[SingleEventData],
    company_events: tuple[SingleEventData, ...],
    embarkation_unit: str,
):
    event_start_date = min(event["date"] for event in main_tunneller_events)
    event_end_date = max(event["date"] for event in main_tunneller_events)

    selected_events: list[SingleEventData] = []
    for event in company_events:
        if (
            event["event"] != "Marched in to the Company Training Camp, Falmouth"
            and event_start_date <= event["date"] <= event_end_date
        ):
            selected_events.append(event)
        if event["event"] == "Marched in to the Company Training Camp, Falmouth" and (
            embarkation_unit == "Main Body" or embarkation_unit == "1st Reinforcements"
        ):
            selected_events.append(event)

    return selected_events


def map_to_event_type(events: list[SingleEventData], lang: str):
    mapped_list: list[Event] = []
    for event in events:
        mapped_list.append(
            Event(
                get_full_date(event["date"], lang),
                EventDetails(event["event"], event["title"], event["image"]),
            )
        )
    return mapped_list


def grouped_by_date(events: list[Event]) -> list[Events]:
    events_grouped_by_date: list[Events] = []

    for event in events:
        event_date: Date = event["date"]
        event_info: EventDetails = event["event"]
        for grouped_event in events_grouped_by_date:
            if grouped_event["date"] == event_date:
                grouped_event["event"].append(event_info)
                break
        else:
            events_grouped_by_date.append(Events(event_date, [event_info]))

    return events_grouped_by_date


def grouped_by_year(grouped_events: list[Events]) -> dict[str, list[Events]]:
    events_grouped_by_year: dict[str, list[Events]] = dict()
    for events in grouped_events:
        year = events["date"]["year"]
        events = Events(
            events["date"],
            events["event"],
        )
        if year in events_grouped_by_year:
            events_grouped_by_year[year].append(events)
        else:
            events_grouped_by_year[year] = list()
            events_grouped_by_year[year].append(events)

    return events_grouped_by_year


def map_front_events(
    company_events: tuple[SingleEventData, ...],
    tunneller_events: tuple[SingleEventData, ...],
    tunneller: MilitaryYearsTunnellerData,
    lang: str,
) -> dict[str, list[Events]]:
    tunneller_events_db: list[SingleEventData] = list(tunneller_events)

    tunneller_events_list: list[SingleEventData] = list(
        tunneller_events_db
        + add_transports(
            Transport(
                tunneller["transport_uk_start"],
                tunneller["transport_uk_ref"],
                tunneller["transport_uk_vessel"],
                "Transfer to England",
            ),
            Transport(
                tunneller["transport_nz_start"],
                tunneller["transport_nz_ref"],
                tunneller["transport_nz_vessel"],
                "Transfer to New Zealand",
            ),
        )
        + add_end_of_service(
            EndOfServiceData(
                tunneller["transferred_to_date"],
                tunneller["transferred_to_unit"],
                tunneller["demobilization_date"],
                tunneller["discharge_uk"],
                tunneller["has_deserted"],
            )
        )
    )

    company_selected_events: list[SingleEventData] = selected_company_events(
        tunneller_events_list, company_events, tunneller["embarkation_unit"]
    )

    full_tunneller_events: list[SingleEventData] = sorted(
        list(
            company_selected_events
            + tunneller_events_list
            + add_enlistment(
                EnlistmentData(
                    tunneller["training_start"],
                    tunneller["training_location"],
                    tunneller["embarkation_unit"],
                    tunneller["enlistment_date"],
                )
            )
            + add_posted(
                PostedData(
                    tunneller["training_start"],
                    tunneller["training_location"],
                    tunneller["embarkation_unit"],
                    tunneller["posted_date"],
                )
            )
            + add_death(
                DeathData(
                    tunneller["death_type"],
                    tunneller["death_date"],
                    tunneller["death_location"],
                    tunneller["death_town"],
                    tunneller["death_country"],
                    tunneller["death_cause"],
                    tunneller["death_circumstances"],
                    tunneller["cemetery"],
                    tunneller["cemetery_town"],
                    tunneller["cemetery_country"],
                    tunneller["grave"],
                )
            )
        ),
        key=lambda item: item["date"],
    )

    events_to_type_event: list[Event] = map_to_event_type(full_tunneller_events, lang)
    events_grouped_by_date: list[Events] = grouped_by_date(events_to_type_event)
    events_grouped_by_year: dict[str, list[Events]] = grouped_by_year(
        events_grouped_by_date
    )

    return events_grouped_by_year


def map_medals(medals: tuple[MedalData, ...]) -> list[Medal]:
    return [
        Medal(medal["name"], medal["country"], medal["image"], medal["citation"])
        for medal in medals
    ]
