# -*- coding: utf-8 -*-
from typing import Optional


def translate_superscript(string: Optional[str], lang: str) -> Optional[str]:
    if string is not None:
        if lang == "fr":
            if "re " in string:
                return string.replace(
                    "re ",
                    "\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}",
                )
            if "er " in string:
                return string.replace(
                    "er ",
                    "\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}",
                )
            if "e " in string:
                return string.replace(
                    "e ", "\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}"
                )
        return string
    return None


def translate_transport_ref(transport_reference: str, lang: str) -> str:
    if lang == "fr":
        if transport_reference == "S.S. Ruapehu 18 December 1915":
            return "S.S. Ruapehu 18 décembre 1915"
        if transport_reference == "Hospital Ship":
            return "Navire-hôpital"
        if transport_reference == "Troop Ship":
            return "Navire de transport de troupes"
    return transport_reference


def translate_family(family: Optional[str], lang: str) -> Optional[str]:
    if family is not None:
        if lang == "en":
            return "{} {}".format(family, "family")
        if lang == "fr":
            return "{} {}".format("Famille", family)
    return None
