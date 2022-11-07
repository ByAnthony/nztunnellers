# -*- coding: utf-8 -*-

from ....models.pre_war_years import ArmyExperience
from ....models.helpers.date_helpers import convert_month_year
from ....models.helpers.pre_war_years_helpers import map_army_experience


country_col = {"en": "New Zealand", "fr": "Nouvelle-Zélande"}
conflict_col = {"en": "South African War", "fr": "Guerre d'Afrique du Sud"}

experience_en = [
    ArmyExperience(
        "Garrison Artillery Volunteers",
        "New Zealand",
        None,
        "12",
    ),
    ArmyExperience(
        None,
        None,
        "South African War",
        "250",
    ),
]
experience_fr = [
    ArmyExperience(
        "National Reserve",
        "Nouvelle-Zélande",
        "Guerre d'Afrique du Sud",
        "50",
    ),
]


def test_map_army_experience_if_army_experience_is_in_en():
    assert map_army_experience(experience_en, "en") == [
        ArmyExperience(
            "Garrison Artillery Volunteers",
            country_col["en"],
            None,
            convert_month_year("12", "en"),
        ),
        ArmyExperience(
            None,
            None,
            conflict_col["en"],
            convert_month_year("250", "en"),
        ),
    ]


def test_map_army_experience_if_army_experience_is_in_fr():
    assert map_army_experience(experience_fr, "fr") == [
        ArmyExperience(
            "National Reserve",
            country_col["fr"],
            conflict_col["fr"],
            convert_month_year("50", "fr"),
        )
    ]


def test_map_army_experience_if_army_experience_is_none_and_lang_is_en():
    assert map_army_experience([], "en") == []


def test_map_army_experience_if_army_experience_is_none_and_lang_is_fr():
    assert map_army_experience([], "fr") == []
