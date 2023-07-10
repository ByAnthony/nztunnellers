# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Section:
    title: str
    text: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Image:
    file: str
    title: Optional[str]
    photographer: Optional[str]
    reference: Optional[str]
    alt: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Next:
    url: str
    chapter: int
    title: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Article:
    id: str
    chapter: int
    title: str
    section: list[Section]
    image: list[Image]
    next: Next
    notes: str

    def __getitem__(self, key: str):
        return getattr(self, key)
