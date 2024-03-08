# -*- coding: utf-8 -*-


from typing import Optional


from ...db.models.ArticleDt import ArticleReferenceDt, FileDt, ImageDt, SectionDt
from ...models.article import Next, Section, Image


def get_images(images: list[FileDt], position: int) -> str:
    if 0 <= position < len(images):
        return images[position].get("file")  # type: ignore
    return ""


def map_sections(sections: list[SectionDt]) -> list[Section]:
    return [Section(section["title"], section["text"]) for section in sections]


def map_images(images: list[ImageDt]) -> list[Image]:
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


def getNextChapter(chapter: int, articles: list[ArticleReferenceDt]) -> Optional[Next]:
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
