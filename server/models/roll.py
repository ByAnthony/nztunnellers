# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Name:
    forename: str
    surname: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Roll:
    id: int
    serial: str
    name: Name

    def __getitem__(self, key: str):
        return getattr(self, key)
