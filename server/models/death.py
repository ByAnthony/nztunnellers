# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .date import Date


@dataclass
class Cemetery:
    name: str
    location: str
    country: str
    grave_reference: Optional[str] = None


@dataclass
class DeathCause:
    type: Optional[str] = None
    circumstances: Optional[str] = None


@dataclass
class DeathPlace:
    location: Optional[str] = None
    town: Optional[str] = None
    country: Optional[str] = None


@dataclass
class Death:
    date: Optional[Date] = None
    place: Optional[DeathPlace] = None
    cause: Optional[DeathCause] = None
    cemetery: Optional[Cemetery] = None
    age_at_death: Optional[int] = None
