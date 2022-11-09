# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .death import Death


@dataclass
class PostWarYears:
    death: Death
