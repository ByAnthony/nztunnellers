# -*- coding: utf-8 -*-
from ....models.military_years import Medal, Training, TransferredToTunnellers
from ....models.helpers.military_years_helpers import (
    get_detachment,
    get_section,
    get_training,
    get_transferred_to_tunnellers,
    get_transport_reference,
    map_medals,
)


def test_get_training():
    assert get_training("1917", "26 January", "Wellington", "Camp") == Training(
        "1917", "26 January", "Wellington", "Camp"
    )


def test_get_transferred_to_tunnellers_if_details_exist():
    assert get_transferred_to_tunnellers(
        "1918", "4 May", "Infantry"
    ) == TransferredToTunnellers("1918", "4 May", "Infantry")


def test_do_not_get_transferred_to_tunnellers_if_details_do_not_exist():
    assert get_transferred_to_tunnellers(None, None, None) is None


def test_get_detachment_if_lang_is_en():
    assert get_detachment("1st Reinforcements", "en") == "1st Reinforcements"


def test_get_detachment_if_lang_is_fr_and_er_renfort():
    assert (
        get_detachment("1er renfort", "fr")
        == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}renfort"
    )


def test_get_detachment_if_lang_is_fr_and_e_renfort():
    assert (
        get_detachment("3e renfort", "fr")
        == "3\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}renfort"
    )


def test_get_section_if_lang_is_en():
    assert get_section("Section No.1", "en") == "Section No.1"


def test_get_section_if_lang_is_fr_and_re_section():
    assert (
        get_section("1re section", "fr")
        == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}section"
    )


def test_get_section_if_lang_is_fr_and_e_section():
    assert (
        get_section("2e section", "fr")
        == "2\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}section"
    )


def test_do_not_get_section_if_section_is_none_and_lang_is_en():
    assert get_section(None, "en") is None


def test_do_not_get_section_if_section_is_none_and_lang_is_fr():
    assert get_section(None, "fr") is None


def test_get_transport_reference_if_transport_is_ruapehu_and_lang_is_en():
    assert (
        get_transport_reference("S.S. Ruapehu 18 December 1915", "en")
        == "S.S. Ruapehu 18 December 1915"
    )


def test_get_transport_reference_if_transport_is_ruapehu_and_lang_is_fr():
    assert (
        get_transport_reference("S.S. Ruapehu 18 December 1915", "fr")
        == "S.S. Ruapehu 18 décembre 1915"
    )


def test_get_transport_reference_if_transport_is_not_ruapehu_and_lang_is_en():
    assert get_transport_reference("HMNZT Tahiti", "en") == "HMNZT Tahiti"


def test_get_transport_reference_if_transport_is_not_ruapehu_and_lang_is_fr():
    assert get_transport_reference("HMNZT Tahiti", "fr") == "HMNZT Tahiti"


british_war_medal = Medal("British War Medal", "United Kingdom", "For bravery")
victory_medal = Medal("Victory Medal", "United Kingdom", None)


def test_map_medals():
    assert map_medals([british_war_medal, victory_medal]) == [
        Medal("British War Medal", "United Kingdom", "For bravery"),
        Medal("Victory Medal", "United Kingdom", None),
    ]


def test_if_medals_do_not_exist_returns_empty_list():
    assert map_medals([]) == []
