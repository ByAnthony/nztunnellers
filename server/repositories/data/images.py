# -*- coding: utf-8 -*-
from typing import Optional
from ...models.helpers.date_helpers import format_date_to_day_month_and_year
from ...models.helpers.image_helpers import (
    get_image,
    get_image_source,
    get_image_source_archives,
    get_image_source_auckland_libraries,
    get_image_source_book,
    get_image_source_family,
    get_image_source_newspaper,
    get_image_url,
)
from ...models.image import Image, ImageBookAuthors
from ...models.tunneller import Tunneller


def images(
    tunneller_result: Tunneller, book_authors_result: list[ImageBookAuthors], lang: str
) -> Optional[Image]:
    return get_image(
        get_image_url(tunneller_result["image"]),
        get_image_source(
            get_image_source_auckland_libraries(
                tunneller_result["image_source_auckland_libraries"]
            ),
            get_image_source_archives(
                tunneller_result["archives_name"],
                tunneller_result["archives_ref"],
            ),
            get_image_source_family(tunneller_result["family_name"], lang),
            get_image_source_newspaper(
                tunneller_result["newspaper_name"],
                format_date_to_day_month_and_year(
                    tunneller_result["newspaper_date"], lang
                ),
            ),
            get_image_source_book(
                book_authors_result,
                tunneller_result["book_title"],
                tunneller_result["book_town"],
                tunneller_result["book_publisher"],
                tunneller_result["book_year"],
                tunneller_result["book_page"],
            ),
        ),
    )
