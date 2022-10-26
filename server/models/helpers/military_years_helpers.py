from typing import Optional
from models.helpers.translator_helpers import translate_superscript, translate_transport_ref
from models.military_years import Medal


def get_transferred_to_tunnellers(posted_year: Optional[str], posted_date: Optional[str], posted_from: Optional[str]) -> Optional[dict[Optional[str], Optional[str]]]:
    if posted_date and posted_from is not None:
        return {'posted_year': posted_year, 'posted_date': posted_date, 'posted_from': posted_from}
    return None


def get_detachment(detachment: str, lang: str) -> Optional[str]:
    return translate_superscript(detachment, lang)


def get_section(section: Optional[str], lang: str) -> Optional[str]:
    return translate_superscript(section, lang)


def get_training(start_year: str, start_date: str, location: str, location_type: str) -> dict[str, str, str]:
    return {'start_year': start_year, 'start_date': start_date, 'location': location, 'location_type': location_type}


def get_transport_reference(transport_reference: str, lang: str) -> str:
    return translate_transport_ref(transport_reference, lang)


def map_medals(medals: tuple[Medal]) -> list[Medal]:
    return [Medal(medal['medal_name'], medal['medal_citation'], medal['country']) for medal in medals]
