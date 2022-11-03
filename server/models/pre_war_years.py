# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass()
class ArmyExperience:
    unit: Optional[str] = None
    country: Optional[str] = None
    conflict: Optional[str] = None
    duration: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Employment:
    occupation: str
    employer: Optional[str] = None


@dataclass
class PreWarYear:
    army_experience: list[ArmyExperience]
    employment: Employment
    residence: Optional[str] = None
    marital_status: Optional[str] = None
    wife: Optional[str] = None
    religion: Optional[str] = None
