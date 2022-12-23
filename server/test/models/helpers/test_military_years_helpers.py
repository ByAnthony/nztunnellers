# -*- coding: utf-8 -*-
from ....models.death import Cemetery, Death, DeathCause, DeathPlace
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
    get_cemetery,
    get_death_circumstances,
    get_death_place,
    get_death_war,
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


class TestGetTraining:
    def test_if_training_exists(self):
        assert get_training(
            Date("1917", "26{}January".format(no_break_space)), "Wellington", "Camp"
        ) == Training(
            Date("1917", "26{}January".format(no_break_space)), "Wellington", "Camp"
        )

    def test_if_training_does_not_exist(self):
        assert get_training(None, "Wellington", "Camp") is None


class TestGetTransferred:
    def test_if_details_exist(self):
        assert get_transferred_to_tunnellers(
            Date("1918", "4{}May".format(no_break_space)), "Infantry"
        ) == TransferredToTunnellers(
            Date("1918", "4{}May".format(no_break_space)), "Infantry"
        )

    def test_if_details_do_not_exist(self):
        assert get_transferred_to_tunnellers(None, None) is None


class TestGetDetachment:
    def test_if_lang_is_en(self):
        assert get_detachment("1st Reinforcements", "en") == "1st Reinforcements"

    def test_if_lang_is_fr_and_er_renfort(self):
        assert get_detachment(
            "1er renfort", "fr"
        ) == "1\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}{}renfort".format(
            no_break_space
        )

    def test_if_lang_is_fr_and_e_renfort(self):
        assert get_detachment(
            "3e renfort", "fr"
        ) == "3\N{MODIFIER LETTER SMALL E}{}renfort".format(no_break_space)


class TestGetSection:
    class TestGetSectionIf:
        def test_get_section_if_lang_is_en(self):
            assert get_section("Section No.1", "en") == "Section No.1"

        def test_get_section_if_lang_is_fr_and_re_section(self):
            assert get_section(
                "1re section", "fr"
            ) == "1\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}{}section".format(
                no_break_space
            )

        def test_get_section_if_lang_is_fr_and_e_section(self):
            assert get_section(
                "2e section", "fr"
            ) == "2\N{MODIFIER LETTER SMALL E}{}section".format(no_break_space)

    class TestDoNotGetSectionIf:
        def test_section_is_none_and_lang_is_en(self):
            assert get_section(None, "en") is None

        def test_section_is_none_and_lang_is_fr(self):
            assert get_section(None, "fr") is None


class TestGetTransportReference:
    def test_transport_is_ruapehu_and_lang_is_en(self):
        assert get_transport_reference(ruapehu, "en") == ruapehu

    def test_transport_is_ruapehu_and_lang_is_fr(self):
        assert get_transport_reference(ruapehu, "fr") == "S.S. Ruapehu 18 décembre 1915"

    def test_transport_is_hospital_ship_and_lang_is_en(self):
        assert get_transport_reference(hospital_ship, "en") == hospital_ship

    def test_transport_is_hospital_ship_and_lang_is_fr(self):
        assert get_transport_reference(hospital_ship, "fr") == "Navire-hôpital"

    def test_transport_is_troop_ship_and_lang_is_en(self):
        assert get_transport_reference(troop_ship, "en") == troop_ship

    def test_transport_is_troop_ship_and_lang_is_fr(self):
        assert (
            get_transport_reference(troop_ship, "fr")
            == "Navire de transport de troupes"
        )

    def test_transport_is_not_ruapehu_and_lang_is_en(self):
        assert get_transport_reference(tahiti, "en") == tahiti

    def test_transport_is_not_ruapehu_and_lang_is_fr(self):
        assert get_transport_reference(tahiti, "fr") == tahiti


class TestGetDeserter:
    def test_if_has_deserted_is_true(self):
        assert get_boolean(1) is True

    def test_if_has_deserted_is_false(self):
        assert get_boolean(0) is False

    def test_if_has_deserted_is_none(self):
        assert get_boolean(None) is False


class TestGetTransferredTo:
    def test_if_data_exists(self):
        assert get_transferred_to("1962-09-27", "NZ Infantry", "en") == Transferred(
            Date("1962", "27{}September".format(no_break_space)), "NZ Infantry"
        )

    def test_if_data_is_none_and_lang_is_en(self):
        assert get_transferred_to(None, None, "en") is None

    def test_if_data_is_none_and_lang_is_fr(self):
        assert get_transferred_to(None, None, "fr") is None


demobilization = Demobilization(
    Date("1919", "26{}January".format(no_break_space)), "New Zealand"
)


class TestGetEndOfService:
    def test_if_data_exists(self):
        assert (
            get_end_of_service(
                Date("1919", "26{}January".format(no_break_space)), "New Zealand"
            )
            == demobilization
        )

    def test_if_data_is_none(self):
        assert get_end_of_service(None, "New Zealand") is None


class TestGetEndOfServiceCountry:
    def test_if_discharge_uk_is_true_and_lang_is_en(self):
        assert get_end_of_service_country(True, "en") == "United Kingdom"

    def test_if_discharge_uk_is_true_and_lang_is_fr(self):
        assert get_end_of_service_country(True, "fr") == "Royaume-Uni"

    def test_if_discharge_uk_is_false_and_lang_is_en(self):
        assert get_end_of_service_country(False, "en") == "New Zealand"

    def test_if_discharge_uk_is_false_and_lang_is_fr(self):
        assert get_end_of_service_country(False, "fr") == "Nouvelle-Zélande"


class TestGetDeathWar:
    def test_if_death_is_death_war(self):
        assert get_death_war(
            "War",
            Date("1918", "09-12"),
            DeathPlace("Battlefield", "Arras", "France"),
            DeathCause("Killed in Action", "In the performance of his duty"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
        ) == Death(
            Date("1918", "09-12"),
            DeathPlace("Battlefield", "Arras", "France"),
            DeathCause("Killed in Action", "In the performance of his duty"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
        )

    def test_if_death_is_not_death_war(self):
        assert (
            get_death_war(
                "War injury",
                Date("1918", "09-12"),
                DeathPlace("Battlefield", "Arras", "France"),
                DeathCause("Killed in Action", "In the performance of his duty"),
                Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
            )
            is None
        )


class TestGetDeathPlace:
    def test_if_death_place_exists(self):
        assert get_death_place("Battlefield", "Arras", "France") == DeathPlace(
            "Battlefield", "Arras", "France"
        )

    def test_if_location_does_not_exist(self):
        assert get_death_place(None, "Arras", "France") == DeathPlace(
            None, "Arras", "France"
        )

    def test_if_town_does_not_exist(self):
        assert get_death_place("Battlefield", None, "France") == DeathPlace(
            "Battlefield", None, "France"
        )

    def test_if_country_does_not_exist(self):
        assert get_death_place("Battlefield", "Arras", None) == DeathPlace(
            "Battlefield", "Arras", None
        )

    def test_if_death_place_does_not_exist(self):
        assert get_death_place(None, None, None) is None


class TestGetDeathCircumstances:
    def test_if_cause_and_circumstances_exist(self):
        assert get_death_circumstances(
            "Killed in Action", "In the performance of his duty"
        ) == DeathCause("Killed in Action", "In the performance of his duty")

    def test_if_cause_does_not_exist_and_circumstances_exist(self):
        assert get_death_circumstances("Killed in Action", None) == DeathCause(
            "Killed in Action", None
        )

    def test_if_cause_and_circumstances_do_not_exist(self):
        assert get_death_circumstances(None, None) is None


class TestGetCemetery:
    def test_if_cemetery_data_exits(self):
        assert get_cemetery(
            "Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"
        ) == Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref")

    def test_if_cemetery_name_does_not_exit(self):
        assert get_cemetery(None, "Auckland", "New Zealand", "Gr. Ref") is None


british_war_medal = Medal("British War Medal", "United Kingdom", "For bravery")
victory_medal = Medal("Victory Medal", "United Kingdom", None)


class TestMapMedals:
    def test_if_medals_exist(self):
        assert map_medals([british_war_medal, victory_medal]) == [
            Medal("British War Medal", "United Kingdom", "For bravery"),
            Medal("Victory Medal", "United Kingdom", None),
        ]

    def test_if_empty_list(self):
        assert map_medals([]) == []
