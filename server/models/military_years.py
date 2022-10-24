from dataclasses import dataclass
from typing import Optional


@dataclass
class Medal:
    name: Optional[str]
    citation: Optional[str]
    country: Optional[str]


@dataclass
class Transport:
    transport_reference: str
    vessel: str
    departure_year: str
    departure_date: str
    departure_port: Optional[str]
    arrival_year: Optional[str]
    arrival_date: Optional[str]
    arrival_port: Optional[str]


@dataclass
class Training:
    start_year: str
    start_date: str
    location: str
    location_type: str


@dataclass
class EmbarkationUnit:
    detachment: str
    section: Optional[str]
    attached_corps: Optional[str]
    training: Training


@dataclass
class TransferredToTunnellers:
    posted_year: Optional[str]
    posted_date: Optional[str]
    posted_from: Optional[str]


@dataclass
class Enlistment:
    enlistment_year: Optional[str]
    enlistment_date: Optional[str]
    military_district: Optional[str]
    alias: Optional[str]
    transferred_to_tunnellers: Optional[TransferredToTunnellers]
    rank: str


@dataclass
class MilitaryYears:
    enlistment: Enlistment
    embarkation_unit: EmbarkationUnit
    transport_uk: Transport
    medals: list[Optional[Medal]]
