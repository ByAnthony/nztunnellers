# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class AboutUsData:
    id: str
    title: str

    def __getitem__(self, key: str):
        return getattr(self, key)
