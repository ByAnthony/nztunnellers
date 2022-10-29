# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class ImageBookAuthors:
    forename: str
    surname: str


@dataclass
class ImageBook:
    authors: list[ImageBookAuthors]
    title: str
    town: str
    publisher: str
    year: str
    page: Optional[str]


@dataclass
class ImageNewspaper:
    name: str
    date: str


@dataclass
class ImageArchives:
    location: str
    reference: str


@dataclass
class Source:
    auckland_libraries: Optional[str] = None
    archives: Optional[ImageArchives] = None
    family: Optional[str] = None
    newspaper: Optional[ImageNewspaper] = None
    book: Optional[ImageBook] = None


@dataclass
class Image:
    url: str
    source: Optional[Source] = None
