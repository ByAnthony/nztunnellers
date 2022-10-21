import dataclasses
import json

from dataclasses import dataclass
from models.roll import Roll
from models.origins import Origins
from models.pre_war_years import PreWarYear
from models.military_years import MilitaryYears


@dataclass
class Tunneller(Roll):
    origins: Origins
    pre_war_years: PreWarYear
    military_years: MilitaryYears
    # image: Image
    # sources: Sources


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
