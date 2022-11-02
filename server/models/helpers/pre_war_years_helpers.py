# -*- coding: utf-8 -*-
from ..helpers.date_helpers import convert_month_year
from ..pre_war_years import ArmyExperience


def map_army_experience(
    experiences: tuple[ArmyExperience], lang: str
) -> list[ArmyExperience]:
    return [
        ArmyExperience(
            experience["army_experience_name"],
            experience["country"],
            experience["conflict_name"],
            convert_month_year(experience["army_experience_in_month"], lang),
        )
        for experience in experiences
    ]
