# -*- coding: utf-8 -*-
from typing import Optional

from ...db.models.ArticleData import (
    ArticleReferenceData,
    FileData,
    ImageData,
    SectionData,
)
from ...models.article import Next, Section, Image


def get_images(images: tuple[FileData], position: int) -> str:
    if 0 <= position < len(images):
        return images[position]["file"]
    return ""


def map_sections(sections: tuple[SectionData]) -> list[Section]:
    return [Section(section["title"], section["text"]) for section in sections]


def map_images(images: tuple[ImageData]) -> list[Image]:
    return [
        Image(
            image["file"],
            image["title"],
            image["photographer"],
            image["reference"],
            image["alt"],
        )
        for image in images
    ]


def get_next_chapter(
    chapter: int, articles: tuple[ArticleReferenceData]
) -> Optional[Next]:
    for i in range(len(articles)):
        if articles[i]["chapter"] == chapter:
            if i + 1 < len(articles):
                next_article = articles[i + 1]
                return Next(
                    next_article["id"],
                    next_article["chapter"],
                    next_article["title"],
                )
            else:
                return None
    return None
