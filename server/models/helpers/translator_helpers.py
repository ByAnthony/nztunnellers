# -*- coding: utf-8 -*-
import re
from typing import Optional


def translate_superscript(string: Optional[str], lang: str) -> Optional[str]:
    if string is not None:
        if lang == "fr":

            superscript = {
                "re ": "\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}",
                "er ": "\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}",
                "e ": "\N{MODIFIER LETTER SMALL E}",
                None: None,
            }
            no_break_space = "\N{NO-BREAK SPACE}"
            patterns = ["(?<=1)re ", "(?<=1)er ", "(?<=[0-9])e "]

            def find_superscript(patterns: list[str], text: str) -> Optional[str]:
                for pattern in patterns:
                    result = re.search(pattern, text)
                    if result is not None:
                        return result.group()
                return None

            def find_pattern(patterns: list[str], text: Optional[str]) -> str:
                if text is not None:
                    for pattern in patterns:
                        if re.search(pattern, text) is not None:
                            return pattern
                return "None"

            replace = (
                f"{superscript[find_superscript(patterns, string)]}{no_break_space}"
            )

            return re.sub(find_pattern(patterns, string), replace, string)

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


def translate_town(town: Optional[str], lang: str) -> Optional[str]:
    if town is not None:
        if lang == "fr" and town == "London":
            return "Londres"
    return town


def translate_family(family: Optional[str], lang: str) -> Optional[str]:
    if family is not None:
        if lang == "en":
            return f"{family} {'family'}"
        if lang == "fr":
            return f"{'Famille'} {family}"
    return None
