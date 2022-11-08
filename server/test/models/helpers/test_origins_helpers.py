# -*- coding: utf-8 -*-
from ....models.helpers.origins_helpers import get_nz_resident, get_parent
from ....models.origins import Parent


def test_get_parent_if_name_and_origin_exist():
    assert get_parent("John Doe", "Scotland") == Parent("John Doe", "Scotland")


def test_get_parent_if_only_name_exists():
    assert get_parent("John Doe", None) == Parent("John Doe", None)


def test_get_parent_if_parent_does_not_exist():
    assert get_parent(None, None) is None


def test_get_nz_resident_if_more_than_24_months_and_lang_is_en():
    assert get_nz_resident("168", "en") == "14\N{NO-BREAK SPACE}years"


def test_get_nz_resident_if_more_than_24_months_and_lang_is_fr():
    assert get_nz_resident("168", "fr") == "14\N{NO-BREAK SPACE}ans"


def test_get_nz_resident_if_between_2_and_24_months_and_lang_is_en():
    assert get_nz_resident("16", "en") == "16\N{NO-BREAK SPACE}months"


def test_get_nz_resident_if_between_2_and_24_months_and_lang_is_fr():
    assert get_nz_resident("16", "fr") == "16\N{NO-BREAK SPACE}mois"


def test_get_nz_resident_if_1_month_and_lang_is_en():
    assert get_nz_resident("1", "en") == "1\N{NO-BREAK SPACE}month"


def test_get_nz_resident_if_1_month_and_lang_is_fr():
    assert get_nz_resident("1", "fr") == "1\N{NO-BREAK SPACE}mois"


def test_do_not_get_nz_resident_if_month_is_none_and_lang_is_en():
    assert get_nz_resident(None, "en") is None


def test_do_not_get_nz_resident_if_month_is_none_and_lang_is_fr():
    assert get_nz_resident(None, "fr") is None
