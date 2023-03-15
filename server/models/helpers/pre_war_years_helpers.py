# -*- coding: utf-8 -*-
from .date_helpers import convert_month_in_duration
from ..pre_war_years import ArmyExperience


def map_army_experience(
    experiences: list[ArmyExperience], lang: str
) -> list[ArmyExperience]:
    return [
        ArmyExperience(
            experience["unit"],
            experience["country"],
            experience["conflict"],
            convert_month_in_duration(experience["duration"], lang),
        )
        for experience in experiences
    ]
