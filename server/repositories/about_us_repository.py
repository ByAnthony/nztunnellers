# -*- coding: utf-8 -*-
from dacite import from_dict

# flask_mysqldb does not have stub files
from flask_mysqldb import MySQL  # type: ignore
from typing import Optional


from ..db.models.AboutUsData import AboutUsData
from ..db.models.ArticleData import ImageData, SectionData

from ..models.helpers.article_helpers import (
    map_images,
    map_sections,
)


from ..models.about_us import AboutUs
from ..repositories.queries.about_us_query import (
    about_us_image_query,
    about_us_query,
    about_us_section_query,
)

from ..db.run_sql import run_sql


def show(mysql: MySQL) -> Optional[AboutUs]:
    values: list[str] = ["about-us"]

    about_us_sql: str = about_us_query()
    about_us_result: AboutUsData = run_sql(about_us_sql, mysql, values)[0]

    about_us_section_sql = about_us_section_query()
    about_us_section_result: tuple[SectionData, ...] = run_sql(
        about_us_section_sql, mysql, values
    )

    about_us_image_sql = about_us_image_query()
    about_us_image_result: tuple[ImageData, ...] = run_sql(
        about_us_image_sql, mysql, values
    )

    if about_us_result:

        data = {
            "id": about_us_result["id"],
            "title": about_us_result["title"],
            "section": map_sections(about_us_section_result),
            "image": map_images(about_us_image_result),
        }

        return from_dict(data_class=AboutUs, data=data)

    return None
