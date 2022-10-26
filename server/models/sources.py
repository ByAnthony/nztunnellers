from dataclasses import dataclass
from typing import Optional


@dataclass
class LondonGazette:
    date: str
    page: str


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
class Cenotaph:
    reference: str


@dataclass
class NewZealandArchives:
    reference: str
    url: str


@dataclass
class Sources:
    nz_archives: list[NewZealandArchives]
    awmm_cenotaph: Cenotaph
    nominal_roll: NominalRoll
    london_gazette: list[LondonGazette]
