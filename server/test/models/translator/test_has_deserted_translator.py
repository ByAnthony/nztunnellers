from ....models.translator import has_deserted_translator


def test_if_has_deserted_is_true_and_lang_en_returns_en_translation():
    assert has_deserted_translator.translate_has_deserted(
        True, 'en') == 'End of service as deserter'


def test_if_has_deserted_is_true_and_lang_fr_returns_fr_translation():
    assert has_deserted_translator.translate_has_deserted(
        True, 'fr') == 'Libéré du service comme déserteur'


def test_if_has_deserted_is_none_and_lang_en_returns_none():
    assert has_deserted_translator.translate_has_deserted(
        None, 'en') == None


def test_if_has_deserted_is_none_and_lang_fr_returns_none():
    assert has_deserted_translator.translate_has_deserted(
        None, 'fr') == None
