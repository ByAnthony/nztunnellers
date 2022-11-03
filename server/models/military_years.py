# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Medal:
    name: str
    country: str
    citation: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Transport:
    reference: str
    vessel: str
    departure_year: str
    departure_date: str
    departure_port: Optional[str] = None
    arrival_year: Optional[str] = None
    arrival_date: Optional[str] = None
    arrival_port: Optional[str] = None


@dataclass
class Training:
    start_year: str
    start_date: str
    location: str
    location_type: str


@dataclass
class EmbarkationUnit:
    training: Training
    detachment: str
    section: Optional[str] = None
    attached_corps: Optional[str] = None


@dataclass
class TransferredToTunnellers:
    posted_year: str
    posted_date: str
    posted_from: str


@dataclass
class Enlistment:
    rank: str
    year: Optional[str] = None
    date: Optional[str] = None
    district: Optional[str] = None
    alias: Optional[str] = None
    transferred_to_tunnellers: Optional[TransferredToTunnellers] = None


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    medals: list[Medal]
