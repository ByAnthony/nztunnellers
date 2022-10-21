from dataclasses import dataclass
from typing import Optional


@dataclass
class TransferredToTunnellers:
    posted_date: Optional[str]
    posted_from: Optional[str]
