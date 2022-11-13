# -*- coding: utf-8 -*-
from typing import Optional

from ..date import Date

from ..death import Death

from .translator_helpers import (
    translate_superscript,
    translate_transport_ref,
)
from ..military_years import (
    Demobilization,
    Medal,
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
    if (
        transport_reference is not None
        and vessel is not None
        and departure_date is not None
    ):
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
    date: Optional[Date], unit: Optional[str]
) -> Optional[Transferred]:
    if date is not None and unit is not None:
        return Transferred(date, unit)
    return None


def get_death_war(death_type: Optional[int], date: Optional[Date]) -> Optional[Death]:
    if death_type == 1:
        return Death(date)
    else:
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


def map_medals(medals: list[Medal]) -> list[Medal]:
    return [
        Medal(medal["name"], medal["country"], medal["citation"]) for medal in medals
    ]
