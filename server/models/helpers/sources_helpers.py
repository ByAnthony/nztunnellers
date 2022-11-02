# -*- coding: utf-8 -*-
from ..helpers.date_helpers import format_to_day_month_and_year
from ..sources import LondonGazette, NewZealandArchives, NominalRoll


def map_nz_archives(nz_archives: tuple[NewZealandArchives]) -> list[NewZealandArchives]:
    def get_url(online_ref: str) -> str:
        link = (
            "https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R"
        )
        return "{}{}".format(link, online_ref)

    return [
        NewZealandArchives(
            archives["nz_archives_ref"], get_url(archives["nz_archives_url"])
        )
        for archives in nz_archives
    ]


def get_awmm(reference: str) -> str:
    return "{}{}".format(
        "https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/", reference
    )


def get_nominal_roll(volume: str, roll: str, page: str, lang: str) -> NominalRoll:

    no_break_space = "\N{NO-BREAK SPACE}"
    title_1919 = {
        "en": "Nominal Rolls of New Zealand Expeditionary Force",
        "fr": "Liste nominative du corps expéditionnaire néo-zélandais",
    }
    title_1916 = {
        "en": "Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company",
        "fr": "Liste nominative du corps expéditionnaire néo-zélandais, 1915. Compagnie de tunneliers",
    }
    roll_number_col = {"en": "Roll No.", "fr": "Liste n\N{DEGREE SIGN}"}

    if volume and roll is not None:
        return NominalRoll(
            title_1919[lang],
            "Wellington",
            "Government Printer",
            "1914-1919",
            "p.{}{}".format(no_break_space, page),
            "Volume{}{}".format(no_break_space, volume),
            "{}{}".format(roll_number_col[lang], roll),
        )
    else:
        return NominalRoll(
            title_1916[lang],
            "Wellington",
            "Government Printer",
            "1916",
            "p.{}{}".format(no_break_space, page),
        )


def map_london_gazette(
    london_gazette: tuple[LondonGazette], lang: str
) -> list[LondonGazette]:
    return [
        LondonGazette(
            format_to_day_month_and_year(gazette["london_gazette_date"], lang),
            gazette["london_gazette_page"],
        )
        for gazette in london_gazette
    ]
