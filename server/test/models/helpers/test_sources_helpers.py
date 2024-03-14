# -*- coding: utf-8 -*-
from ....db.models.TunnellerData import LondonGazetteData, NewZealandArchivesData
from ....models.helpers.date_helpers import format_date_to_day_month_and_year
from ....models.sources import LondonGazette, NewZealandArchives, NominalRoll
from ....models.helpers.sources_helpers import (
    map_nz_archives,
    get_awmm,
    get_nominal_roll,
    map_london_gazette,
)


actual_nz_archives_1 = NewZealandArchivesData("AABK 18805 W5520 1/0006561", "22280535")
actual_nz_archives_2 = NewZealandArchivesData("AABK 18805 W5520 1/0006563", "22280537")


expected_ref_1 = NewZealandArchives(
    "AABK 18805 W5520 1/0006561",
    "https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R22280535",
)
expected_ref_2 = NewZealandArchives(
    "AABK 18805 W5520 1/0006563",
    "https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R22280537",
)


class TestMapNzArchives:
    class TestMapNzArchivesIf:
        def test_map_nz_archives_if_archives_has_one_record(self):
            assert map_nz_archives([actual_nz_archives_1]) == [expected_ref_1]

        def test_map_nz_archives_if_archives_has_two_records(self):
            assert map_nz_archives([actual_nz_archives_1, actual_nz_archives_2]) == [
                expected_ref_1,
                expected_ref_2,
            ]


class TestDoNotMapNzArchivesIf:
    def test_do_not_map_nz_archives_if_archives_has_no_record(self):
        assert map_nz_archives([]) == []


class TestGetAwmm:
    def test_get_awmm(self):
        assert (
            get_awmm("fake_reference")
            == "https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/fake_reference"
        )


volume = "III"
roll = "75"
page = "3"

en = "en"
fr = "fr"

no_break_space = "\N{NO-BREAK SPACE}"
roll_number_col = {"en": "Roll No.", "fr": "Liste n\N{DEGREE SIGN}"}

title_1919 = {
    "en": "Nominal Rolls of New Zealand Expeditionary Force",
    "fr": "Liste nominative du corps expéditionnaire néo-zélandais",
}
title_1916 = {
    "en": "Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company",
    "fr": "Liste nominative du corps expéditionnaire néo-zélandais, 1915. Compagnie de tunneliers",
}


class TestGetNominalRoll:
    def test_if_volume_and_roll_are_not_none_and_lang_is_en(self):
        assert get_nominal_roll(volume, roll, page, en) == NominalRoll(
            title_1919[en],
            "Wellington",
            "Government Printer",
            "1914-1919",
            f"p.{no_break_space}{page}",
            f"Volume{no_break_space}{volume}",
            f"{roll_number_col[en]}{roll}",
        )

    def test_if_volume_and_roll_are_not_none_and_lang_is_fr(self):
        assert get_nominal_roll(volume, roll, page, fr) == NominalRoll(
            title_1919[fr],
            "Wellington",
            "Government Printer",
            "1914-1919",
            f"p.{no_break_space}{page}",
            f"Volume{no_break_space}{volume}",
            f"{roll_number_col[fr]}{roll}",
        )

    def test_if_volume_and_roll_are_none_and_lang_en(self):
        assert get_nominal_roll(None, None, page, en) == NominalRoll(
            title_1916[en],
            "Wellington",
            "Government Printer",
            "1916",
            f"p.{no_break_space}{page}",
        )

    def test_if_volume_and_roll_are_none_and_lang_fr(self):
        assert get_nominal_roll(None, None, page, fr) == NominalRoll(
            title_1916[fr],
            "Wellington",
            "Government Printer",
            "1916",
            f"p.{no_break_space}{page}",
        )


london_gazette_list = [
    LondonGazetteData("13575", "1917-12-28"),
    LondonGazetteData("29", "1918-01-01"),
]


class TestMapLondonGazette:
    class TestMapLondonGazetteIf:
        def test_london_gazette_is_not_none_and_lang_is_en(self):
            assert map_london_gazette(london_gazette_list, "en") == [
                LondonGazette(
                    "13575", format_date_to_day_month_and_year("1917-12-28", "en")
                ),
                LondonGazette(
                    "29", format_date_to_day_month_and_year("1918-01-01", "en")
                ),
            ]

        def test_london_gazette_is_not_none_and_lang_is_fr(self):
            assert map_london_gazette(london_gazette_list, "fr") == [
                LondonGazette(
                    "13575", format_date_to_day_month_and_year("1917-12-28", "fr")
                ),
                LondonGazette(
                    "29", format_date_to_day_month_and_year("1918-01-01", "fr")
                ),
            ]

    class TestDoNotMapLondonGazetteIf:
        def test_london_gazette_is_none_and_lang_en(self):
            assert map_london_gazette([], "en") == []

        def test_london_gazette_is_none_and_lang_fr(self):
            assert map_london_gazette([], "fr") == []
