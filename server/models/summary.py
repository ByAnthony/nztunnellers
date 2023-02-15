# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .roll import Name


@dataclass
class Summary:
    serial: str
    name: Name
    birth: str
    death: str
