# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Parent:
    name: Optional[str] = None
    origin: Optional[str] = None


@dataclass
class Parents:
    mother: Optional[Parent] = None
    father: Optional[Parent] = None


@dataclass
class BirthDetails:
    year: str
    date: Optional[str] = None
    country: Optional[str] = None


@dataclass
class Origins:
    birth: BirthDetails
    parents: Parents
    in_nz_length: Optional[str] = None
