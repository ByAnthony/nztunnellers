# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .date import Date
from .death import Death


@dataclass
class Transferred:
    date: Date
    unit: str


@dataclass
class Medal:
    name: str
    country: str
    image: str
    citation: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class EventDetails:
    description: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Events:
    date: Date
    event: list[EventDetails]

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Event:
    date: Date
    event: EventDetails

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class SingleEvent:
    date: Date
    event: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None

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
    departure_date: Optional[Date] = None
    departure_port: Optional[str] = None
    arrival_date: Optional[Date] = None
    arrival_port: Optional[str] = None


@dataclass
class EndOfService:
    deserter: bool
    transferred: Optional[Transferred] = None
    death_war: Optional[Death] = None
    transport_nz: Optional[Transport] = None
    demobilization: Optional[Demobilization] = None


@dataclass
class Training:
    date: Date
    location: str
    location_type: str


@dataclass
class EmbarkationUnit:
    detachment: Optional[str] = None
    training: Optional[Training] = None
    section: Optional[str] = None
    attached_corps: Optional[str] = None


@dataclass
class TransferredToTunnellers:
    date: Date
    posted_from: str


@dataclass
class Enlistment:
    serial: str
    rank: str
    date: Optional[Date] = None
    district: Optional[str] = None
    alias: Optional[str] = None
    transferred_to_tunnellers: Optional[TransferredToTunnellers] = None
    age_at_enlistment: Optional[int] = None


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    front_events: list[Events]
    end_of_service: EndOfService
    medals: list[Medal]
