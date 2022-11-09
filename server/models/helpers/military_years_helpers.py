# -*- coding: utf-8 -*-
from typing import Optional

from .translator_helpers import (
    translate_superscript,
    translate_transport_ref,
)
from ..military_years import Medal, Training, TransferredToTunnellers


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


def get_deserter(has_deserted: Optional[int]) -> bool:
    if has_deserted == 1:
        return True
    return False


def map_medals(medals: list[Medal]) -> list[Medal]:
    return [
        Medal(medal["name"], medal["country"], medal["citation"]) for medal in medals
    ]
