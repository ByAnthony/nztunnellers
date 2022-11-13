# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Date:
    year: Optional[str]
    day_month: Optional[str]
