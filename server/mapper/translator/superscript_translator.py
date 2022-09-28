def translate_superscript(string, lang):
    if lang == 'fr':
        if string.__contains__('re '):
            return string.replace(
                're ', '\N{MODIFIER LETTER SMALL R}\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}')
        if string.__contains__('er '):
            return string.replace(
                'er ', '\N{MODIFIER LETTER SMALL E}\N{MODIFIER LETTER SMALL R}\N{NO-BREAK SPACE}')
        if string.__contains__('e '):
            return string.replace(
                'e ', '\N{MODIFIER LETTER SMALL E}\N{NO-BREAK SPACE}')
    return string
