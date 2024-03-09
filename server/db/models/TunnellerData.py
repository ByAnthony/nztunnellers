# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class ArmyExperienceData:
    unit: Optional[str]
    country: Optional[str]
    conflict: Optional[str]
    duration: Optional[str]

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class SingleEventData:
    date: str
    event: Optional[str]
    title: Optional[str]
    image: Optional[str]

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class MedalsData:
    name: str
    country: str
    citation: Optional[str]
    image: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class NewZealandArchivesData:
    reference: str
    url: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class LondonGazetteData:
    page: str
    date: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class BookAuthorsData:
    book_id: str
    forename: str
    surname: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class TunnellerData:
    id: str
    forename: str
    surname: str
    aka: Optional[str]
    serial: str
    birth_date: Optional[str]
    birth_country: Optional[str]
    mother_name: Optional[str]
    mother_origin: Optional[str]
    father_name: Optional[str]
    father_origin: Optional[str]
    nz_resident_in_month: Optional[int]
    marital_status: Optional[str]
    wife_name: Optional[str]
    occupation: Optional[str]
    employer: Optional[str]
    residence: Optional[str]
    religion: Optional[str]
    enlistment_date: Optional[str]
    military_district_name: str
    posted_date: Optional[str]
    posted_from_corps: Optional[str]
    rank: str
    embarkation_unit: str
    section: Optional[str]
    attached_corps: Optional[str]
    training_start: str
    training_location: str
    training_location_type: str
    transport_uk_ref: str
    transport_uk_vessel: str
    transport_uk_start: str
    transport_uk_origin: str
    transport_uk_end: str
    transport_uk_destination: str
    has_deserted: int
    transferred_to_date: Optional[str]
    transferred_to_unit: Optional[str]
    death_type: Optional[str]
    death_date: str
    death_location: Optional[str]
    death_town: Optional[str]
    death_country: Optional[str]
    death_cause: Optional[str]
    death_circumstances: Optional[str]
    cemetery: Optional[str]
    cemetery_town: Optional[str]
    cemetery_country: Optional[str]
    grave: Optional[str]
    transport_nz_ref: Optional[str]
    transport_nz_vessel: Optional[str]
    transport_nz_start: Optional[str]
    transport_nz_origin: Optional[str]
    transport_nz_end: Optional[str]
    transport_nz_destination: Optional[str]
    demobilization_date: Optional[str]
    discharge_uk: Optional[int]
    image: Optional[str]
    image_source_auckland_libraries: Optional[str]
    archives_name: Optional[str]
    archives_ref: Optional[str]
    family_name: Optional[str]
    newspaper_name: Optional[str]
    newspaper_date: Optional[str]
    book_title: Optional[str]
    book_town: Optional[str]
    book_publisher: Optional[str]
    book_year: str
    book_page: int
    awmm_cenotaph: Optional[str]
    nominal_roll_volume: Optional[str]
    nominal_roll_number: Optional[str]
    nominal_roll_page: str

    def __getitem__(self, key: str):
        return getattr(self, key)
