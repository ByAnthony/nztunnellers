# -*- coding: utf-8 -*-
from typing import Optional

from ...models.helpers.image_helpers import (
    get_image,
    get_image_source,
    get_image_source_auckland_libraries,
    get_image_source_family,
    get_image_url,
)
from ...models.image import Image, ImageArchives, ImageBook, ImageNewspaper


def images(
    image: Optional[str],
    image_source_auckland_libraries: Optional[str],
    image_source_archives: Optional[ImageArchives],
    family_name: Optional[str],
    image_source_newspaper: Optional[ImageNewspaper],
    image_source_book: Optional[ImageBook],
    lang: str,
) -> Optional[Image]:
    return get_image(
        get_image_url(image),
        get_image_source(
            get_image_source_auckland_libraries(image_source_auckland_libraries),
            image_source_archives,
            get_image_source_family(family_name, lang),
            image_source_newspaper,
            image_source_book,
        ),
    )
