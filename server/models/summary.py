# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .roll import Name
from .date import Date


@dataclass
class Summary:
    serial: str
    name: Name
    birth: Date
    death: Date
