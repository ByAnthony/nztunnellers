# -*- coding: utf-8 -*-
from dataclasses import dataclass


from .article import ArticleReference


@dataclass
class TunnellerImage:
    id: int
    image: str

    def __getitem__(self, key: str):
        return getattr(self, key)


@dataclass
class Homepage:
    tunnellers: list[TunnellerImage]
    history_chapters: list[ArticleReference]
