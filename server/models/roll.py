# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Name:
    forename: str
    surname: str


@dataclass
class Roll:
    id: int
    serial: str
    name: Name

    def __getitem__(self, key):
        return getattr(self, key)
