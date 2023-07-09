# -*- coding: utf-8 -*-
from typing import Optional
from dacite import from_dict


from ..models.article import Article, Section, Image
from ..repositories.queries.article_query import (
    article_query,
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


def show(id: str, mysql: MySQL) -> Optional[Article]:
    article_sql = article_query()
    values = [id]
    article_result: Article = run_sql(article_sql, mysql, values)[0]

    section_sql = section_query()
    section_result: list[Section] = run_sql(section_sql, mysql, values)

    image_sql = image_query()
    image_result: list[Image] = run_sql(image_sql, mysql, values)

    if article_result:

        data = {
            "id": article_result["id"],
            "title": article_result["title"],
            "section": map_sections(section_result),
            "image": map_images(image_result),
            "notes": article_result["notes"],
        }

        return from_dict(data_class=Article, data=data)

    return None
