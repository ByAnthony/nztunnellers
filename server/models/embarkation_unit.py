from dataclasses import dataclass
from typing import Optional
from models.training import Training


@dataclass
class EmbarkationUnit:
    detachment: str
    section: Optional[str]
    attached_corps: Optional[str]
    training: Training
