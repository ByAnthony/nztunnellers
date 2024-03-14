# -*- coding: utf-8 -*-
from dacite import from_dict

# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL  # type: ignore
from typing import Optional

from ..db.models.ArticleData import (
    ArticleData,
    ArticleReferenceData,
    FileData,
    ImageData,
    SectionData,
)

from ..models.helpers.article_helpers import (
    get_images,
    get_next_chapter,
    map_images,
    map_sections,
)


from ..models.article import Article, ArticleReference
from ..repositories.queries.article_query import (
    article_query,
    next_article_query,
    images_query,
    section_query,
    image_query,
)

from ..db.run_sql import run_sql


def select_all(mysql: MySQL) -> list[ArticleReference]:
    articles: list[ArticleReference] = []

    articles_sql: str = next_article_query()
    articles_results: tuple[ArticleReferenceData] = run_sql(articles_sql, mysql, None)

    images_sql = images_query()
    image_result: tuple[FileData] = run_sql(images_sql, mysql, None)

    next_sql = next_article_query()
    next_result: tuple[ArticleReferenceData] = run_sql(next_sql, mysql, None)

    for index, row in enumerate(articles_results):
        article = ArticleReference(
            row["id"],
            row["chapter"],
            row["title"],
            get_images(image_result, index),
            get_next_chapter(row["chapter"], next_result),
        )
        articles.append(article)
    return articles


def show(id: str, mysql: MySQL) -> Optional[Article]:
    values: list[str] = [id]

    article_sql: str = article_query()
    article_result: ArticleData = run_sql(article_sql, mysql, values)[0]

    section_sql = section_query()
    section_result: tuple[SectionData] = run_sql(section_sql, mysql, values)

    next_sql = next_article_query()
    next_result: tuple[ArticleReferenceData] = run_sql(next_sql, mysql, None)

    image_sql = image_query()
    image_result: tuple[ImageData] = run_sql(image_sql, mysql, values)

    if article_result:

        data = {
            "id": article_result["id"],
            "chapter": article_result["chapter"],
            "title": article_result["title"],
            "section": map_sections(section_result),
            "image": map_images(image_result),
            "next": get_next_chapter(article_result["chapter"], next_result),
            "notes": article_result["notes"],
        }

        return from_dict(data_class=Article, data=data)

    return None
