# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .military_years import Date


@dataclass
class Cemetery:
    name: str
    location: str
    country: str
    grave_reference: str


@dataclass
class DeathCause:
    type: Optional[str] = None
    circumstances: Optional[str] = None


@dataclass
class Death:
    date: Date
    location: Optional[str] = None
    country: Optional[str] = None
    cause: Optional[DeathCause] = None
    cemetery: Optional[Cemetery] = None
