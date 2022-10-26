from typing import Optional


def translate_superscript(string: str, lang: str) -> Optional[str]:
    if string is not None:
        if lang == 'fr':
            if 're ' in string:
                return string.replace(
                    're ', '\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}')
            if 'er ' in string:
                return string.replace(
                    'er ', '\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}')
            if 'e ' in string:
                return string.replace(
                    'e ', '\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}')
        return string


def translate_transport_ref(transport_reference: str, lang: str) -> str:
    if lang == 'fr':
        if transport_reference == 'S.S. Ruapehu 18 December 1915':
            return 'S.S. Ruapehu 18 décembre 1915'
    return transport_reference


def translate_family(family: str, lang: str) -> Optional[str]:
    if family is not None:
        if lang == 'en':
            return '{} {}'.format(family, 'family')
        if lang == 'fr':
            return '{} {}'.format('Famille', family)
    return None
