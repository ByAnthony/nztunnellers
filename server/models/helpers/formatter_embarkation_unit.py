from typing import Optional
from models.helpers.translator_superscript import translate_superscript


def get_detachment(detachment: str, lang: str) -> str:
    return translate_superscript(detachment, lang)


def get_section(section: Optional[str], lang: str) -> Optional[str]:
    return translate_superscript(section, lang)
