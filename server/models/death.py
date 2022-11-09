# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


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
    year: str
    date: str
    location: Optional[str] = None
    country: Optional[str] = None
    cause: Optional[DeathCause] = None
    cemetery: Optional[Cemetery] = None
