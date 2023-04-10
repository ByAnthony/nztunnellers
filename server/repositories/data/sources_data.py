# -*- coding: utf-8 -*-
from ...models.helpers.sources_helpers import (
    get_awmm,
    get_nominal_roll,
    map_london_gazette,
    map_nz_archives,
)
from ...models.sources import LondonGazette, NewZealandArchives, Sources
from ...models.tunneller import Tunneller


def sources(
    nz_archives: list[NewZealandArchives],
    tunneller: Tunneller,
    london_gazette: list[LondonGazette],
    lang: str,
) -> Sources:
    return Sources(
        map_nz_archives(nz_archives),
        get_awmm(tunneller["awmm_cenotaph"]),
        get_nominal_roll(
            tunneller["nominal_roll_volume"],
            tunneller["nominal_roll_number"],
            tunneller["nominal_roll_page"],
            lang,
        ),
        map_london_gazette(london_gazette, lang),
    )
