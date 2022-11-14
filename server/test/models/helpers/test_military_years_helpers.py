# -*- coding: utf-8 -*-
from ....models.date import Date
from ....models.military_years import (
    Demobilization,
    Medal,
    Training,
    Transferred,
    TransferredToTunnellers,
)
from ....models.helpers.military_years_helpers import (
    get_boolean,
    get_detachment,
    get_end_of_service,
    get_end_of_service_country,
    get_section,
    get_training,
    get_transferred_to,
    get_transferred_to_tunnellers,
    get_transport_reference,
    map_medals,
)

no_break_space = "\N{NO-BREAK SPACE}"
ruapehu = "S.S. Ruapehu 18 December 1915"
tahiti = "HMNZT Tahiti"
hospital_ship = "Hospital Ship"
troop_ship = "Troop Ship"


def test_get_training_if_training_exists():
    assert get_training(
        Date("1917", "26{}January".format(no_break_space)), "Wellington", "Camp"
    ) == Training(
        Date("1917", "26{}January".format(no_break_space)), "Wellington", "Camp"
    )


def test_do_not_get_training_if_training_does_not_exist():
    assert get_training(None, "Wellington", "Camp") is None


def test_get_transferred_to_tunnellers_if_details_exist():
    assert get_transferred_to_tunnellers(
        Date("1918", "4{}May".format(no_break_space)), "Infantry"
    ) == TransferredToTunnellers(
        Date("1918", "4{}May".format(no_break_space)), "Infantry"
    )


def test_do_not_get_transferred_to_tunnellers_if_details_do_not_exist():
    assert get_transferred_to_tunnellers(None, None) is None


def test_get_detachment_if_lang_is_en():
    assert get_detachment("1st Reinforcements", "en") == "1st Reinforcements"


def test_get_detachment_if_lang_is_fr_and_er_renfort():
    assert get_detachment(
        "1er renfort", "fr"
    ) == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}{}renfort".format(
        no_break_space
    )


def test_get_detachment_if_lang_is_fr_and_e_renfort():
    assert get_detachment(
        "3e renfort", "fr"
    ) == "3\N{MODIFIER LETTER SMALL E}{}renfort".format(no_break_space)


def test_get_section_if_lang_is_en():
    assert get_section("Section No.1", "en") == "Section No.1"


def test_get_section_if_lang_is_fr_and_re_section():
    assert get_section(
        "1re section", "fr"
    ) == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}{}section".format(
        no_break_space
    )


def test_get_section_if_lang_is_fr_and_e_section():
    assert get_section(
        "2e section", "fr"
    ) == "2\N{MODIFIER LETTER SMALL E}{}section".format(no_break_space)


def test_do_not_get_section_if_section_is_none_and_lang_is_en():
    assert get_section(None, "en") is None


def test_do_not_get_section_if_section_is_none_and_lang_is_fr():
    assert get_section(None, "fr") is None


def test_get_transport_reference_if_transport_is_ruapehu_and_lang_is_en():
    assert get_transport_reference(ruapehu, "en") == ruapehu


def test_get_transport_reference_if_transport_is_ruapehu_and_lang_is_fr():
    assert get_transport_reference(ruapehu, "fr") == "S.S. Ruapehu 18 décembre 1915"


def test_get_transport_reference_if_transport_is_hospital_ship_and_lang_is_en():
    assert get_transport_reference(hospital_ship, "en") == hospital_ship


def test_get_transport_reference_if_transport_is_hospital_ship_and_lang_is_fr():
    assert get_transport_reference(hospital_ship, "fr") == "Navire-hôpital"


def test_get_transport_reference_if_transport_is_troop_ship_and_lang_is_en():
    assert get_transport_reference(troop_ship, "en") == troop_ship


def test_get_transport_reference_if_transport_is_troop_ship_and_lang_is_fr():
    assert get_transport_reference(troop_ship, "fr") == "Navire de transport de troupes"


def test_get_transport_reference_if_transport_is_not_ruapehu_and_lang_is_en():
    assert get_transport_reference(tahiti, "en") == tahiti


def test_get_transport_reference_if_transport_is_not_ruapehu_and_lang_is_fr():
    assert get_transport_reference(tahiti, "fr") == tahiti


def test_get_deserter_if_has_deserted_is_true():
    assert get_boolean(1) is True


def test_get_deserter_if_has_deserted_is_false():
    assert get_boolean(0) is False


def test_get_deserter_if_has_deserted_is_none():
    assert get_boolean(None) is False


def test_get_end_of_service_country_if_discharge_uk_is_true_and_lang_is_en():
    assert get_end_of_service_country(True, "en") == "United Kingdom"


def test_get_end_of_service_country_if_discharge_uk_is_true_and_lang_is_fr():
    assert get_end_of_service_country(True, "fr") == "Royaume-Uni"


def test_get_end_of_service_country_if_discharge_uk_is_false_and_lang_is_en():
    assert get_end_of_service_country(False, "en") == "New Zealand"


def test_get_end_of_service_country_if_discharge_uk_is_false_and_lang_is_fr():
    assert get_end_of_service_country(False, "fr") == "Nouvelle-Zélande"


def test_get_transferred_to_if_data_exists():
    assert get_transferred_to("1962-09-27", "NZ Infantry", "en") == Transferred(
        Date("1962", "27{}September".format(no_break_space)), "NZ Infantry"
    )


def test_do_not_get_transferred_to_if_data_is_none_and_lang_is_en():
    assert get_transferred_to(None, None, "en") is None


def test_do_not_get_transferred_to_if_data_is_none_and_lang_is_fr():
    assert get_transferred_to(None, None, "fr") is None


demobilization = Demobilization(
    Date("1919", "26{}January".format(no_break_space)), "New Zealand"
)


def test_get_end_of_service_if_data_exists():
    assert (
        get_end_of_service(
            Date("1919", "26{}January".format(no_break_space)), "New Zealand"
        )
        == demobilization
    )


def test_do_not_get_end_of_service_if_data_is_none():
    assert get_end_of_service(None, "New Zealand") is None


british_war_medal = Medal("British War Medal", "United Kingdom", "For bravery")
victory_medal = Medal("Victory Medal", "United Kingdom", None)


def test_map_medals():
    assert map_medals([british_war_medal, victory_medal]) == [
        Medal("British War Medal", "United Kingdom", "For bravery"),
        Medal("Victory Medal", "United Kingdom", None),
    ]


def test_if_medals_do_not_exist_returns_empty_list():
    assert map_medals([]) == []
