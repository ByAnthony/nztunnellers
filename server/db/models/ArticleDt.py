# -*- coding: utf-8 -*-
from typing import Optional


class ArticleReferenceDt:
    id: str
    chapter: int
    title: str

    def __getitem__(self, key: str):
        return getattr(self, key)


class FileDt:
    file: str

    def __getitem__(self, key: str):
        return getattr(self, key)


class ArticleDt:
    id: str
    chapter: int
    title: str
    notes: str

    def __getitem__(self, key: str):
        return getattr(self, key)


class SectionDt:
    title: str
    text: str

    def __getitem__(self, key: str):
        return getattr(self, key)


class ImageDt:
    file: str
    title: Optional[str]
    photographer: Optional[str]
    reference: Optional[str]
    alt: str

    def __getitem__(self, key: str):
        return getattr(self, key)
