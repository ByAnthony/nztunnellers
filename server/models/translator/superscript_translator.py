def translate_superscript(string: str, lang: str) -> str:
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
