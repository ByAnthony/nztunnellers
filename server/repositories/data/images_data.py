# -*- coding: utf-8 -*-
from typing import Optional

from ...db.models.TunnellerData import BookAuthorsData, TunnellerData
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
from ...models.image import Image


def images(
    tunneller: TunnellerData, book_authors: tuple[BookAuthorsData], lang: str
) -> Optional[Image]:
    return get_image(
        get_image_url(tunneller["image"]),
        get_image_source(
            get_image_source_auckland_libraries(
                tunneller["image_source_auckland_libraries"]
            ),
            get_image_source_archives(
                tunneller["archives_name"],
                tunneller["archives_ref"],
            ),
            get_image_source_family(tunneller["family_name"], lang),
            get_image_source_newspaper(
                tunneller["newspaper_name"],
                format_date_to_day_month_and_year(tunneller["newspaper_date"], lang),
            ),
            get_image_source_book(
                book_authors,
                tunneller["book_title"],
                tunneller["book_town"],
                tunneller["book_publisher"],
                tunneller["book_year"],
                tunneller["book_page"],
            ),
        ),
    )
