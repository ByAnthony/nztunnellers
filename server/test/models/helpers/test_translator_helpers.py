# -*- coding: utf-8 -*-
from server.models.helpers.translator_helpers import (
    translate_superscript,
    translate_transport_ref,
    translate_family,
)


transport_ruapehu = "S.S. Ruapehu 18 December 1915"
transport_hmnzs = "HMNZS 96"
family = "Williamson"


def test_translate_superscript_re_if_lang_is_fr_and_string_contains_re():
    assert (
        translate_superscript("1re section", "fr")
        == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}section"
    )


def test_translate_superscript_er_if_lang_is_fr_and_string_contains_er():
    assert (
        translate_superscript("1er renfort", "fr")
        == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}renfort"
    )


def test_translate_superscript_e_if_lang_is_fr_and_string_contains_e():
    assert (
        translate_superscript("2e renfort", "fr")
        == "2\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}renfort"
    )


def test_do_not_translate_superscript_if_lang_is_en():
    assert translate_superscript("2nd Reinforcement", "en") == "2nd Reinforcement"


def test_do_not_translate_superscript_if_lang_is_fr_and_string_is_none():
    assert translate_superscript(None, "fr") == None


def test_do_not_translate_superscript_if_lang_is_en_and_string_is_none():
    assert translate_superscript(None, "en") == None


def test_translate_superscript_if_transport_is_ruapehu_and_lang_is_fr():
    assert (
        translate_transport_ref(transport_ruapehu, "fr")
        == "S.S. Ruapehu 18 décembre 1915"
    )


def test_do_not_translate_transport_ref_if_transport_is_not_ruapehu_and_lang_is_fr():
    assert translate_transport_ref(transport_hmnzs, "fr") == transport_hmnzs


def test_do_not_translate_transport_ref_if_transport_is_ruapehu_and_lang_is_en():
    assert translate_transport_ref(transport_ruapehu, "en") == transport_ruapehu


def test_do_not_translate_transport_ref_if_transport_is_not_ruapehu_and_lang_is_en():
    assert translate_transport_ref(transport_hmnzs, "en") == transport_hmnzs


def test_translate_family_if_family_is_not_none_and_lang_is_en():
    assert translate_family(family, "en") == "{} {}".format(family, "family")


def test_translate_family_if_family_is_not_none_and_lang_is_fr():
    assert translate_family(family, "fr") == "{} {}".format("Famille", family)


def test_do_not_translate_family_if_family_is_none_and_lang_is_en():
    assert translate_family(None, "en") == None


def test_do_not_translate_family_if_family_is_none_and_lang_is_fr():
    assert translate_family(None, "fr") == None