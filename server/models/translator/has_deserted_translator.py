def translate_has_deserted(value: bool or None, lang: str) -> str or None:
    if value == True:
        if lang == 'en':
            return 'End of service as deserter'
        if lang == 'fr':
            return 'Libéré du service comme déserteur'
    return None
