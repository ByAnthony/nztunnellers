def translate_family(family: str, lang: str) -> str or None:
    if family is not None:
        if lang == 'en':
            return '{} {}'.format(family, 'family')
        if lang == 'fr':
            return '{} {}'.format('Famille', family)
    return None
