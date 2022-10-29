# -*- coding: utf-8 -*-
from typing import Optional

from models.helpers.translator_helpers import (
    translate_superscript,
    translate_transport_ref,
)
from models.military_years import Medal, Training, TransferredToTunnellers


def get_training(
    start_year: str, start_date: str, location: str, location_type: str
) -> Training:
    return Training(start_year, start_date, location, location_type)


def get_transferred_to_tunnellers(
    posted_year: str, posted_date: str, posted_from: str
) -> Optional[TransferredToTunnellers]:
    if posted_date and posted_from is not None:
        return TransferredToTunnellers(posted_year, posted_date, posted_from)
    return None


def get_detachment(detachment: str, lang: str) -> Optional[str]:
    return translate_superscript(detachment, lang)


def get_section(section: str, lang: str) -> Optional[str]:
    return translate_superscript(section, lang)


def get_transport_reference(transport_reference: str, lang: str) -> str:
    return translate_transport_ref(transport_reference, lang)


def map_medals(medals: tuple[Medal]) -> list[Medal]:
    return [
        Medal(medal["medal_name"], medal["country"], medal["medal_citation"])
        for medal in medals
    ]
