from dataclasses import dataclass
from typing import Optional
from models.helpers.date_formatter import format_date
from models.transferred_to_tunnellers import TransferredToTunnellers


@dataclass
class Enlistment(TransferredToTunnellers):
    enlistment_date: Optional[str]
    military_district: Optional[str]
    alias: Optional[str]
    transferred_to_tunnellers: TransferredToTunnellers
    rank: str

    def get_enlistment(enlistment_date: Optional[str], military_district: Optional[str], alias: Optional[str], transferred_to_tunnellers: TransferredToTunnellers, rank: str) -> dict[Optional[str], Optional[str], Optional[str], TransferredToTunnellers, str]:
        return {'enlistment_date': format_date(enlistment_date), 'military_district': military_district, 'alias': alias, 'transferred_to_tunnellers': transferred_to_tunnellers, 'rank': rank}
