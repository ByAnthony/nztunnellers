# -*- coding: utf-8 -*-
def article_query() -> str:
    return """SELECT
        article.string_id AS id
        , article.id AS chapter
        , article.title AS title
        , article.notes AS notes

        FROM article

        WHERE article.string_id=%s"""


def section_query() -> str:
    return """SELECT
        article_section.title AS title
        , article_section.text AS text

        FROM article_section
        JOIN article_section_join ON article_section_join.section_id=article_section.id

        WHERE article_section_join.article_id=%s"""


def image_query() -> str:
    return """SELECT
        article_image.file AS file
        , article_image.title AS title
        , article_image.photographer AS photographer
        , article_image.reference AS reference
        , article_image.alt AS alt

        FROM article_image
        JOIN article_image_join ON article_image_join.image_id=article_image.id

        WHERE article_image_join.article_id=%s"""


def articles_query() -> str:
    return """SELECT
        article.string_id AS id
        , article.id AS chapter
        , article.title AS title

        FROM article
    """
