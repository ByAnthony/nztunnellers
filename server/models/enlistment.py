from dataclasses import dataclass
from typing import Optional
from models.transferred_to_tunnellers import TransferredToTunnellers


@dataclass
class Enlistment:
    enlistment_date: Optional[str]
    military_district: Optional[str]
    alias: Optional[str]
    transferred_to_tunnellers: Optional[TransferredToTunnellers]
    rank: str
