# -*- coding: utf-8 -*-
class TunnellerDt:
    id: str
    surname: str
    forename: str
    serial: str
    birth_date: str
    death_date: str

    def __getitem__(self, key: str):
        return getattr(self, key)
