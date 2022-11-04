# -*- coding: utf-8 -*-
from server.models.sources import NewZealandArchives
from server.models.helpers.sources_helpers import map_nz_archives, get_awmm


actual_nz_archives_1 = NewZealandArchives("AABK 18805 W5520 1/0006561", "22280535")
actual_nz_archives_2 = NewZealandArchives("AABK 18805 W5520 1/0006563", "22280537")


expected_ref_1 = NewZealandArchives(
    "AABK 18805 W5520 1/0006561",
    "https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R22280535",
)
expected_ref_2 = NewZealandArchives(
    "AABK 18805 W5520 1/0006563",
    "https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R22280537",
)


def test_map_nz_archives_if_archives_has_one_record():
    assert map_nz_archives([actual_nz_archives_1]) == [expected_ref_1]


def test_map_nz_archives_if_archives_has_two_records():
    assert map_nz_archives([actual_nz_archives_1, actual_nz_archives_2]) == [
        expected_ref_1,
        expected_ref_2,
    ]


def test_do_not_map_nz_archives_if_archives_has_no_record():
    assert map_nz_archives([]) == []


def test_get_awmm():
    assert (
        get_awmm("fake_reference")
        == "https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/fake_reference"
    )
