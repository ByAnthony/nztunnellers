# -*- coding: utf-8 -*-
from ....db.models.TunnellerData import ArmyExperienceData
from ....models.pre_war_years import ArmyExperience
from ....models.helpers.date_helpers import convert_month_in_duration
from ....models.helpers.pre_war_years_helpers import map_army_experience


country_col = {"en": "New Zealand", "fr": "Nouvelle-Zélande"}
conflict_col = {"en": "South African War", "fr": "Guerre d'Afrique du Sud"}

experience_en = (
    ArmyExperienceData(
        "Garrison Artillery Volunteers",
        "New Zealand",
        None,
        "12",
    ),
    ArmyExperienceData(
        None,
        None,
        "South African War",
        "250",
    ),
)
experience_fr = (
    ArmyExperienceData(
        "National Reserve",
        "Nouvelle-Zélande",
        "Guerre d'Afrique du Sud",
        "50",
    ),
)


class TestMapArmyExperience:
    def test_if_army_experience_is_in_en(self):
        assert map_army_experience(experience_en, "en") == [
            ArmyExperience(
                "Garrison Artillery Volunteers",
                country_col["en"],
                None,
                convert_month_in_duration("12", "en"),
            ),
            ArmyExperience(
                None,
                None,
                conflict_col["en"],
                convert_month_in_duration("250", "en"),
            ),
        ]

    def test_if_army_experience_is_in_fr(self):
        assert map_army_experience(experience_fr, "fr") == [
            ArmyExperience(
                "National Reserve",
                country_col["fr"],
                conflict_col["fr"],
                convert_month_in_duration("50", "fr"),
            )
        ]

    def test_if_army_experience_is_empty_list_and_lang_is_en(self):
        assert map_army_experience((), "en") == []

    def test_if_army_experience_is_empty_list_and_lang_is_fr(self):
        assert map_army_experience((), "fr") == []
