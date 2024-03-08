# -*- coding: utf-8 -*-
import dataclasses
import json

from typing import Any


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        try:
            return super().default(o)
        except TypeError:
            return str(o)
