# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


from .summary import Summary
from .image import Image
from .origins import Origins
from .military_years import MilitaryYears
from .post_service_years import PostServiceYears
from .pre_war_years import PreWarYear
from .sources import Sources


@dataclass
class Tunneller:
    id: int
    summary: Summary
    origins: Origins
    pre_war_years: PreWarYear
    military_years: MilitaryYears
    post_service_years: PostServiceYears
    sources: Sources
    image: Optional[Image] = None

    def __getitem__(self, key: str):
        return getattr(self, key)
