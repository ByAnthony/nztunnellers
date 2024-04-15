# -*- coding: utf-8 -*-
from dataclasses import dataclass

from ..models.article import Image, Section


@dataclass
class AboutUs:
    id: str
    title: str
    section: list[Section]
    image: list[Image]

    def __getitem__(self, key: str):
        return getattr(self, key)
