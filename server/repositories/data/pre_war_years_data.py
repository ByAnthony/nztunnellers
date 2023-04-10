# -*- coding: utf-8 -*-
from ...models.helpers.pre_war_years_helpers import map_army_experience
from ...models.tunneller import Tunneller
from ...models.pre_war_years import ArmyExperience, Employment, PreWarYear


def pre_war_years(
    army_experience: list[ArmyExperience], tunneller: Tunneller, lang: str
) -> PreWarYear:
    return PreWarYear(
        map_army_experience(army_experience, lang),
        Employment(tunneller["occupation"], tunneller["employer"]),
        tunneller["residence"],
        tunneller["marital_status"],
        tunneller["wife_name"],
        tunneller["religion"],
    )
