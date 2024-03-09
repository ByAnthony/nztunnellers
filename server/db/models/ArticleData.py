# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class ArticleReferenceData:
    id: str
    chapter: int
    title: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class FileData:
    file: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class ArticleData:
    id: str
    chapter: int
    title: str
    notes: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class SectionData:
    title: str
    text: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class ImageData:
    file: str
    title: Optional[str]
    photographer: Optional[str]
    reference: Optional[str]
    alt: str

    def __getitem__(self, key: str):
        return getattr(self, key)
