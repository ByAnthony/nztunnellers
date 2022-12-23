# -*- coding: utf-8 -*-
from ....models.post_service_years import DeathAfterService
from ....models.death import Cemetery, DeathCause, DeathPlace
from ....models.date import Date
from ....models.helpers.post_service_years_helpers import get_death


class TestGetDeathWar:
    def test_if_death_is_death_war(self):
        assert (
            get_death(
                "War",
                Date("1918", "09-12"),
                DeathPlace("Battlefield", "Arras", "France"),
                DeathCause("Killed in Action", "In the performance of his duty"),
                Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
            )
            is None
        )

    def test_if_death_is_war_injury(self):
        assert get_death(
            "War injuries",
            Date("1918", "09-12"),
            DeathPlace("Battlefield", "Arras", "France"),
            DeathCause("Killed in Action", "In the performance of his duty"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
        ) == DeathAfterService(
            Date("1918", "09-12"),
            DeathPlace("Battlefield", "Arras", "France"),
            DeathCause("Killed in Action", "In the performance of his duty"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
            True,
        )

    def test_if_death_is_after_war(self):
        assert get_death(
            "After war",
            Date("1928", "09-12"),
            DeathPlace(None, "Arras", "France"),
            DeathCause(None, "Heart attack"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
        ) == DeathAfterService(
            Date("1928", "09-12"),
            DeathPlace(None, "Arras", "France"),
            DeathCause(None, "Heart attack"),
            Cemetery("Cemetery Name", "Auckland", "New Zealand", "Gr. Ref"),
            False,
        )

    def test_if_death_data_does_not_exist(self):
        assert (
            get_death(
                None,
                None,
                None,
                None,
                None,
            )
            is None
        )
