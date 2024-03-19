# -*- coding: utf-8 -*-
from ...db.models.TunnellerData import (
    LondonGazetteData,
    NewZealandArchivesData,
)
from ...models.helpers.sources_helpers import (
    get_awmm,
    map_london_gazette,
    map_nz_archives,
)
from ...models.sources import NominalRoll, Sources


def sources(
    nz_archives: tuple[NewZealandArchivesData],
    awmm_cenotaph: str,
    nominal_roll: NominalRoll,
    london_gazette: tuple[LondonGazetteData],
    lang: str,
) -> Sources:
    return Sources(
        map_nz_archives(nz_archives),
        get_awmm(awmm_cenotaph),
        nominal_roll,
        map_london_gazette(london_gazette, lang),
    )
