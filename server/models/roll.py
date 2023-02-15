# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Name:
    forename: str
    surname: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Roll:
    id: int
    name: Name
    birth: Optional[str]
    death: Optional[str]

    def __getitem__(self, key: str):
        return getattr(self, key)
