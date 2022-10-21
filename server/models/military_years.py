from dataclasses import dataclass
from models.enlistment import Enlistment
from models.embarkation_unit import EmbarkationUnit
from models.transport import Transport
from models.medals import Medal


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    medals: tuple[Medal]
