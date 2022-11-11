# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .military_years import Date


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
    date: Optional[Date] = None
    country: Optional[str] = None


@dataclass
class Origins:
    birth: BirthDetails
    parents: Parents
    in_nz_length: Optional[str] = None
