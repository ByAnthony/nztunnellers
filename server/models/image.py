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
    page: Optional[int]


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
    auckland_libraries: Optional[str]
    archives: Optional[ImageArchives]
    family: Optional[str]
    newspaper: Optional[ImageNewspaper]
    book: Optional[ImageBook]


@dataclass
class Image:
    url: Optional[str]
    source: Optional[Source]
