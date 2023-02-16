# -*- coding: utf-8 -*-
from ...models.helpers.pre_war_years_helpers import map_army_experience
from ...models.tunneller import Tunneller
from ...models.pre_war_years import ArmyExperience, Employment, PreWarYear


def pre_war_years(
    army_experience_result: list[ArmyExperience], tunneller_result: Tunneller, lang: str
) -> PreWarYear:
    return PreWarYear(
        map_army_experience(army_experience_result, lang),
        Employment(tunneller_result["occupation"], tunneller_result["employer"]),
        tunneller_result["residence"],
        tunneller_result["marital_status"],
        tunneller_result["wife_name"],
        tunneller_result["religion"],
    )
