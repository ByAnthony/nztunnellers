from dataclasses import dataclass
from typing import Optional
from models.helpers.superscript_translator import translate_superscript
from models.training import Training


@dataclass
class EmbarkationUnit(Training):
    detachment: str
    section: Optional[str]
    attached_corps: Optional[str]
    training: Training

    def get_embarkation_unit(detachment: str, section: Optional[str], attached_corps: Optional[str], training: Training) -> dict[str, Optional[str], Optional[str], Training]:
        return {'detachment': detachment, 'section': section, 'attached_corps': attached_corps, 'training': training}

    def get_detachment(detachment: str, lang: str) -> str:
        return translate_superscript(detachment, lang)

    def get_section(section: Optional[str], lang: str) -> Optional[str]:
        return translate_superscript(section, lang)
