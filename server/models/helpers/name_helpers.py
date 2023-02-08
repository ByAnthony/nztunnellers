# -*- coding: utf-8 -*-
def set_surname_to_uppercase(surname: str):
    if surname.startswith("Mc"):
        return "Mc" + surname[2:].upper()
    return surname.upper()
