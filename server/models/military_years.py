from dataclasses import dataclass
from models.enlistment import Enlistment
from models.embarkation_unit import EmbarkationUnit


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: dict
    medals: list[dict]

    def get_military_years(enlistment: Enlistment, embarkation_unit: EmbarkationUnit) -> dict[Enlistment, EmbarkationUnit]:
        return {'enlistment': enlistment, 'embarkation_unit': embarkation_unit}
