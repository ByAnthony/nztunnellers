from dataclasses import dataclass
from models.enlistment import Enlistment
from models.embarkation_unit import EmbarkationUnit
from models.transport import Transport


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    medals: list[dict]

    def get_military_years(enlistment: Enlistment, embarkation_unit: EmbarkationUnit, transport_uk: Transport) -> dict[Enlistment, EmbarkationUnit, Transport]:
        return {'enlistment': enlistment, 'embarkation_unit': embarkation_unit, 'transport_uk': transport_uk}
