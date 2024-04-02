# -*- coding: utf-8 -*-
from ....models.helpers.translator_helpers import (
    translate_superscript,
    translate_town,
    translate_transport_ref,
    translate_family,
)


transport_ruapehu = "S.S. Ruapehu 18 December 1915"
hospital_ship = "Hospital Ship"
troop_ship = "Troop Ship"
transport_hmnzs = "HMNZS 96"
town = "London"
family = "Williamson"


class TestTranslateSuperscript:
    class TestTranslateIf:
        def test_lang_is_fr_and_string_contains_re(self):
            assert (
                translate_superscript("1re section", "fr")
                == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}section"
            )

        def test_lang_is_fr_and_string_contains_er(self):
            assert (
                translate_superscript("1er renfort", "fr")
                == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}renfort"
            )

        def test_lang_is_fr_and_string_contains_none(self):
            assert (
                translate_superscript("2e renfort", "fr")
                == "2\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}renfort"
            )

        def test_lang_is_fr_and_string_is_none(self):
            assert translate_superscript("compagnie", "fr") == "compagnie"

    class TestDoNotTranslateIf:
        def test_lang_is_en(self):
            assert (
                translate_superscript("2nd Reinforcement", "en") == "2nd Reinforcement"
            )

        def test_lang_is_fr_and_string_is_none(self):
            assert translate_superscript(None, "fr") is None

        def test_lang_is_en_and_string_is_none(self):
            assert translate_superscript(None, "en") is None


class TestTranslateTransport:
    class TestTranslateIf:
        def test_transport_is_ruapehu_and_lang_is_fr(self):
            assert (
                translate_transport_ref(transport_ruapehu, "fr")
                == "S.S. Ruapehu 18 décembre 1915"
            )

        def test_transport_is_hospital_ship_and_lang_is_fr(self):
            assert translate_transport_ref(hospital_ship, "fr") == "Navire-hôpital"

        def test_transport_is_troop_ship_and_lang_is_fr(self):
            assert (
                translate_transport_ref(troop_ship, "fr")
                == "Navire de transport de troupes"
            )

    class TestDoNotTranslateIf:
        def test_transport_is_ruapehu_and_lang_is_en(self):
            assert translate_transport_ref(transport_ruapehu, "en") == transport_ruapehu

        def test_transport_is_hospital_ship_and_lang_is_en(self):
            assert translate_transport_ref(hospital_ship, "en") == hospital_ship

        def test_transport_is_troop_ship_and_lang_is_en(self):
            assert translate_transport_ref(troop_ship, "en") == troop_ship

        def test_transport_is_not_ruapehu_and_lang_is_fr(self):
            assert translate_transport_ref(transport_hmnzs, "fr") == transport_hmnzs

        def test_transport_is_not_ruapehu_and_lang_is_en(self):
            assert translate_transport_ref(transport_hmnzs, "en") == transport_hmnzs


class TestTranslateTown:
    class TestTranslateIf:
        def test_town_is_london_and_lang_is_fr(self):
            assert translate_town(town, "fr") == "Londres"

    class TestDoNotTranslateIf:
        def test_town_is_london_and_lang_is_en(self):
            assert translate_town(town, "en") == "London"

        def test_town_is_not_london_and_lang_is_fr(self):
            assert translate_town("Arras", "fr") == "Arras"

        def test_town_is_not_london_and_lang_is_en(self):
            assert translate_town("Glasgow", "fr") == "Glasgow"


class TestTranslateFamily:
    class TestTranslateIf:
        def test_family_is_not_none_and_lang_is_en(self):
            assert translate_family(family, "en") == f"Courtesy of {family} family"

        def test_family_is_not_none_and_lang_is_fr(self):
            assert translate_family(family, "fr") == f"Courtoisie de la famille {family}"

    class TestDoNotTranslateIf:
        def test_family_is_none_and_lang_is_en(self):
            assert translate_family(None, "en") is None

        def test_family_is_none_and_lang_is_fr(self):
            assert translate_family(None, "fr") is None
