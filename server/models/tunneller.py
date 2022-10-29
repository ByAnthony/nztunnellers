# -*- coding: utf-8 -*-
import dataclasses
import json
from dataclasses import dataclass
from typing import Optional

from models.image import Image
from models.military_years import MilitaryYears
from models.origins import Origins
from models.pre_war_years import PreWarYear
from models.roll import Roll
from models.sources import Sources


@dataclass
class Tunneller(Roll):
    origins: Origins
    pre_war_years: PreWarYear
    military_years: MilitaryYears
    sources: Sources
    image: Optional[Image] = None


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Roll or Tunneller):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
