# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Date:
    year: Optional[str] = None
    day_month: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)
