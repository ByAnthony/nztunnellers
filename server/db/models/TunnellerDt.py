# -*- coding: utf-8 -*-
from typing import Optional


class TunnellerDt:
    id: str
    surname: str
    forename: str
    serial: str
    birth_date: Optional[str]
    death_date: Optional[str]

    def __getitem__(self, key: str):
        return getattr(self, key)
