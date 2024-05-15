# -*- coding: utf-8 -*-
# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL  # type: ignore


from ..models.homepage import Homepage, TunnellerImage

from ..db.models.ArticleData import (
    ArticleReferenceData,
    FileData,
)

from ..models.helpers.article_helpers import (
    get_images,
    get_next_chapter,
)


from ..models.article import ArticleReference
from ..repositories.queries.article_query import (
    next_article_query,
    images_query,
)
from ..repositories.queries.tunnellers_images_query import tunnellers_images_query

from ..db.run_sql import run_sql


def get_homepage(mysql: MySQL) -> Homepage:
    tunnellers: list[TunnellerImage] = []

    images_sql: str = tunnellers_images_query()
    images_results: tuple[TunnellerImage, ...] = run_sql(images_sql, mysql, None)

    for index, row in enumerate(images_results):
        image = TunnellerImage(
            row["id"],
            row["image"],
        )
        tunnellers.append(image)

    articles: list[ArticleReference] = []

    articles_sql: str = next_article_query()
    articles_results: tuple[ArticleReferenceData, ...] = run_sql(
        articles_sql, mysql, None
    )
    images_sql = images_query()
    image_result: tuple[FileData, ...] = run_sql(images_sql, mysql, None)
    next_sql = next_article_query()
    next_result: tuple[ArticleReferenceData, ...] = run_sql(next_sql, mysql, None)

    for index, row in enumerate(articles_results):
        article = ArticleReference(
            row["id"],
            row["chapter"],
            row["title"],
            get_images(image_result, index),
            get_next_chapter(row["chapter"], next_result),
        )
        articles.append(article)

    return Homepage(tunnellers, articles)
