# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Date:
    year: Optional[str]
    day_month: Optional[str]


@dataclass
class Transferred:
    date: Date
    unit: str


@dataclass
class Medal:
    name: str
    country: str
    citation: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class FrontEvents:
    date: Date
    event: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Demobilization:
    date: Date
    country: str


@dataclass
class Transport:
    reference: str
    vessel: str
    departure_date: Date
    departure_port: Optional[str] = None
    arrival_date: Optional[Date] = None
    arrival_port: Optional[str] = None


@dataclass
class EndOfService:
    deserter: bool
    transferred: Optional[Transferred] = None
    # death_war: Optional[Death] = None
    transport_nz: Optional[Transport] = None
    demobilization: Optional[Demobilization] = None


@dataclass
class Training:
    date: Date
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
    date: Date
    posted_from: str


@dataclass
class Enlistment:
    rank: str
    date: Date
    district: Optional[str] = None
    alias: Optional[str] = None
    transferred_to_tunnellers: Optional[TransferredToTunnellers] = None


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    # front_events: list[FrontEvents]
    end_of_service: EndOfService
    medals: list[Medal]
