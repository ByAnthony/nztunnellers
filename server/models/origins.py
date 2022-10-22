from dataclasses import dataclass
from typing import Optional


@dataclass
class Parent:
    name: Optional[str]
    origin: Optional[str]


@dataclass
class Parents:
    mother: Optional[Parent]
    father: Optional[Parent]


@dataclass
class BirthDetails:
    year: Optional[str]
    date: Optional[str]
    country: Optional[str]


@dataclass
class Origins:
    birth: BirthDetails
    parents: Parents
    in_nz_length: Optional[str]
