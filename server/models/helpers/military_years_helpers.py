# -*- coding: utf-8 -*-
from typing import Optional

from .translator_helpers import (
    translate_superscript,
    translate_transport_ref,
)
from ..military_years import (
    Demobilization,
    Medal,
    Training,
    TransferredToTunnellers,
    Transport,
)


def get_training(
    start_year: Optional[str],
    start_date: Optional[str],
    location: str,
    location_type: str,
) -> Optional[Training]:
    if start_year is not None and start_date is not None:
        return Training(start_year, start_date, location, location_type)
    return None


def get_transferred_to_tunnellers(
    posted_year: Optional[str], posted_date: Optional[str], posted_from: Optional[str]
) -> Optional[TransferredToTunnellers]:
    if posted_year is not None and posted_date is not None and posted_from is not None:
        return TransferredToTunnellers(posted_year, posted_date, posted_from)
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
    departure_year: Optional[str],
    departure_date: Optional[str],
    departure_port: Optional[str],
    arrival_year: Optional[str],
    arrival_date: Optional[str],
    arrival_port: Optional[str],
) -> Optional[Transport]:
    if (
        transport_reference is not None
        and vessel is not None
        and departure_year is not None
        and departure_date is not None
    ):
        return Transport(
            transport_reference,
            vessel,
            departure_year,
            departure_date,
            departure_port,
            arrival_year,
            arrival_date,
            arrival_port,
        )
    return None


def get_boolean(data: Optional[int]) -> bool:
    if data == 1:
        return True
    return False


def get_end_of_service(
    service_end_year: Optional[str], service_end_date: Optional[str], country: str
) -> Optional[Demobilization]:
    if service_end_year is not None and service_end_date is not None:
        return Demobilization(service_end_year, service_end_date, country)
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
