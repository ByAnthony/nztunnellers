# -*- coding: utf-8 -*-
from ...db.models.TunnellerData import ArmyExperienceData, TunnellerData
from ...models.helpers.pre_war_years_helpers import map_army_experience
from ...models.pre_war_years import Employment, PreWarYear


def pre_war_years(
    army_experience: tuple[ArmyExperienceData], tunneller: TunnellerData, lang: str
) -> PreWarYear:
    return PreWarYear(
        map_army_experience(army_experience, lang),
        Employment(tunneller["occupation"], tunneller["employer"]),
        tunneller["residence"],
        tunneller["marital_status"],
        tunneller["wife_name"],
        tunneller["religion"],
    )
