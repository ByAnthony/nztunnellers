# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .date import Date


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
    date: Optional[Date] = None
    # location: Optional[str] = None
    # country: Optional[str] = None
    # cause: Optional[DeathCause] = None
    # cemetery: Optional[Cemetery] = None
