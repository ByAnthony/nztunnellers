# -*- coding: utf-8 -*-
from ..helpers.date_helpers import convert_month_year
from ..pre_war_years import ArmyExperience


def map_army_experience(
    experiences: tuple[ArmyExperience], lang: str
) -> list[ArmyExperience]:
    return [
        ArmyExperience(
            experience["unit"],
            experience["country"],
            experience["conflict"],
            convert_month_year(experience["duration"], lang),
        )
        for experience in experiences
    ]
