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
    nz_archives_result: list[NewZealandArchives],
    tunneller_result: Tunneller,
    london_gazette_result: list[LondonGazette],
    lang: str,
) -> Sources:
    return Sources(
        map_nz_archives(nz_archives_result),
        get_awmm(tunneller_result["awmm_cenotaph"]),
        get_nominal_roll(
            tunneller_result["nominal_roll_volume"],
            tunneller_result["nominal_roll_number"],
            tunneller_result["nominal_roll_page"],
            lang,
        ),
        map_london_gazette(london_gazette_result, lang),
    )
