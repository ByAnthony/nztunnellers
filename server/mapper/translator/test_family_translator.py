from . import family_translator


family = 'Williamson'


def test_if_family_is_not_none_and_lang_en_returns_family_and_name():
    assert family_translator.translate_family(
        family, 'en') == '{} {}'.format(family, 'family')


def test_if_family_is_not_none_and_lang_fr_returns_family_and_name():
    assert family_translator.translate_family(
        family, 'fr') == '{} {}'.format('Famille', family)


def test_if_family_is_none_and_lang_en_returns_none():
    assert family_translator.translate_family(
        None, 'en') == None


def test_if_family_is_none_and_lang_fr_returns_none():
    assert family_translator.translate_family(
        None, 'fr') == None
