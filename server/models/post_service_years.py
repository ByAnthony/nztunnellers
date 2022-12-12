# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional
from .death import Death


@dataclass
class DeathAfterService(Death):
    death_war_injury: Optional[bool] = None


@dataclass
class PostServiceYears:
    death: Optional[DeathAfterService] = None
