# -*- coding: utf-8 -*-
def about_us_query() -> str:
    return """SELECT
        about_us.string_id AS id
        , about_us.title AS title

        FROM about_us

        WHERE about_us.string_id=%s"""


def about_us_section_query() -> str:
    return """SELECT
        about_us_section.title AS title
        , about_us_section.text AS text

        FROM about_us_section
        JOIN about_us_section_join ON about_us_section_join.about_us_section_id=about_us_section.id

        WHERE about_us_section_join.about_us_id=%s"""


def about_us_image_query() -> str:
    return """SELECT
        about_us_image.file AS file
        , about_us_image.title AS title
        , about_us_image.photographer AS photographer
        , about_us_image.reference AS reference
        , about_us_image.alt AS alt

        FROM about_us_image
        JOIN about_us_image_join ON about_us_image_join.about_us_image_id=about_us_image.id

        WHERE about_us_image_join.about_us_id=%s"""
