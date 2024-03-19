# -*- coding: utf-8 -*-
from typing import Optional
from ...db.models.TunnellerData import ArmyExperienceData
from ...models.helpers.pre_war_years_helpers import map_army_experience
from ...models.pre_war_years import Employment, PreWarYear


def pre_war_years(
    army_experience: tuple[ArmyExperienceData],
    employment: Employment,
    residence: Optional[str],
    marital_status: Optional[str],
    wife_name: Optional[str],
    religion: Optional[str],
    lang: str,
) -> PreWarYear:
    return PreWarYear(
        map_army_experience(army_experience, lang),
        employment,
        residence,
        marital_status,
        wife_name,
        religion,
    )
