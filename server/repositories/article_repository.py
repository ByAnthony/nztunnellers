# -*- coding: utf-8 -*-
from typing import Optional
from dacite import from_dict

from ..models.helpers.article_helpers import getNextChapter


from ..models.article import Article, Next, Section, Image
from ..repositories.queries.article_query import (
    article_query,
    articles_query,
    section_query,
    image_query,
)

from ..db.run_sql import run_sql
from flask_mysqldb import MySQL


def map_sections(sections: list[Section]) -> list[Section]:
    return [Section(section["title"], section["text"]) for section in sections]


def map_images(images: list[Image]) -> list[Image]:
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


def select_all(mysql: MySQL) -> list[Next]:
    articles: list[Next] = []
    articles_sql = articles_query()
    results: list[Next] = run_sql(articles_sql, mysql, None)

    for row in results:
        article = Next(row["id"], row["chapter"], row["title"])
        articles.append(article)
    return articles


def show(id: str, mysql: MySQL) -> Optional[Article]:
    article_sql = article_query()
    values = [id]
    article_result: Article = run_sql(article_sql, mysql, values)[0]

    section_sql = section_query()
    section_result: list[Section] = run_sql(section_sql, mysql, values)

    next_sql = articles_query()
    next_result: list[Article] = run_sql(next_sql, mysql, None)

    image_sql = image_query()
    image_result: list[Image] = run_sql(image_sql, mysql, values)

    if article_result:

        data = {
            "id": article_result["id"],
            "chapter": article_result["chapter"],
            "title": article_result["title"],
            "section": map_sections(section_result),
            "image": map_images(image_result),
            "next": getNextChapter(article_result["chapter"], next_result),
            "notes": article_result["notes"],
        }

        return from_dict(data_class=Article, data=data)

    return None
