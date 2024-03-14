# -*- coding: utf-8 -*-
from ...db.models.TunnellerData import (
    LondonGazetteData,
    NewZealandArchivesData,
    TunnellerData,
)
from ...models.helpers.sources_helpers import (
    get_awmm,
    get_nominal_roll,
    map_london_gazette,
    map_nz_archives,
)
from ...models.sources import Sources


def sources(
    nz_archives: tuple[NewZealandArchivesData],
    tunneller: TunnellerData,
    london_gazette: tuple[LondonGazetteData],
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
