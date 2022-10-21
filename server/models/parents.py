from dataclasses import dataclass
from typing import Optional
from .parent import Parent


@dataclass
class Parents:
    mother: Optional[Parent]
    father: Optional[Parent]
