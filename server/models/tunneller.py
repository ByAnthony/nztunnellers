# -*- coding: utf-8 -*-
import dataclasses
import json
from dataclasses import dataclass
from typing import Any, Optional

from .image import Image
from .military_years import MilitaryYears
from .origins import Origins
from .post_service_years import PostServiceYears
from .pre_war_years import PreWarYear
from .roll import Roll
from .sources import Sources


@dataclass
class Tunneller(Roll):
    origins: Origins
    pre_war_years: PreWarYear
    military_years: MilitaryYears
    post_service_years: PostServiceYears
    sources: Sources
    image: Optional[Image] = None

    def __getitem__(self, key: str):
        return getattr(self, key)


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
