# -*- coding: utf-8 -*-
import re
from typing import Optional


def translate_superscript(string: Optional[str], lang: str) -> Optional[str]:
    if string is not None:
        if lang == "fr":
            no_break_space = "\N{NO-BREAK SPACE}"

            if re.search("(?<=[0-9])re ", string):
                superscript_re = (
                    "\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}"
                )
                replace = "{}{}".format(superscript_re, no_break_space)
                return re.sub("(?<=[0-9])re ", replace, string)

            elif re.search("(?<=[0-9])er ", string):
                superscript_er = (
                    "\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}"
                )
                replace = "{}{}".format(superscript_er, no_break_space)
                return re.sub("(?<=[0-9])er ", replace, string)

            elif re.search("(?<=[0-9])e ", string):
                superscript_e = "\N{MODIFIER LETTER SMALL E}"
                replace = "{}{}".format(superscript_e, no_break_space)
                return re.sub("(?<=[0-9])e ", replace, string)

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
