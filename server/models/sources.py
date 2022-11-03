# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class LondonGazette:
    date: str
    page: str

    def __getitem__(self, key):
        return getattr(self, key)


@dataclass
class NominalRoll:
    title: str
    town: str
    publisher: str
    date: str
    page: str
    volume: Optional[str] = None
    roll: Optional[str] = None


@dataclass
class NewZealandArchives:
    reference: str
    url: str

    def __getitem__(self, key):
        return getattr(self, key)


@dataclass
class Sources:
    nz_archives: list[NewZealandArchives]
    awmm_cenotaph: str
    nominal_roll: NominalRoll
    london_gazette: list[LondonGazette]
