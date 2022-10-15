from ....models.translator import transport_ref_translator


transport_ruapehu = 'S.S. Ruapehu 18 December 1915'
transport_hmnzs = 'HMNZS 96'


def test_if_transport_ruapehu_and_lang_fr_returns_transport_in_french():
    assert transport_ref_translator.translate_transport_ref(
        transport_ruapehu, 'fr') == 'S.S. Ruapehu 18 décembre 1915'


def test_if_transport_ruapehu_and_lang_en_returns_transport_in_english():
    assert transport_ref_translator.translate_transport_ref(
        transport_ruapehu, 'en') == transport_ruapehu


def test_if_transport_not_ruapehu_and_lang_en_returns_transport():
    assert transport_ref_translator.translate_transport_ref(
        transport_hmnzs, 'en') == transport_hmnzs


def test_if_transport_not_ruapehu_and_lang_fr_returns_transport():
    assert transport_ref_translator.translate_transport_ref(
        transport_hmnzs, 'fr') == transport_hmnzs
