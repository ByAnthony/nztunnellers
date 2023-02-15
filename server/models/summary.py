# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional
from .roll import Name


@dataclass
class Summary:
    name: Name
    birth: Optional[str]
    death: Optional[str]
