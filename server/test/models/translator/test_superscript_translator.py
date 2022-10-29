# -*- coding: utf-8 -*-
from ....models.helpers import translator_superscript


def test_if_lang_fr_and_string_contains_re_returns_superscript_re():
    assert (
        translator_superscript.translate_superscript("1re section", "fr")
        == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}section"
    )


def test_if_lang_fr_and_string_contains_er_returns_superscript_er():
    assert (
        translator_superscript.translate_superscript("1er renfort", "fr")
        == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}renfort"
    )


def test_if_lang_fr_and_string_contains_er_returns_superscript_e():
    assert (
        translator_superscript.translate_superscript("2e renfort", "fr")
        == "2\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}renfort"
    )


def test_if_lang_en_returns_string():
    assert (
        translator_superscript.translate_superscript("2nd Reinforcement", "en")
        == "2nd Reinforcement"
    )


def test_if_string_is_none_returns_none():
    assert translator_superscript.translate_superscript(None, "en") == None


def test_if_string_is_none_returns_none():
    assert translator_superscript.translate_superscript(None, "fr") == None
