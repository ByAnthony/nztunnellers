def translate_transport_ref(transport_reference, lang):
    if lang == 'fr':
        if transport_reference == 'S.S. Ruapehu 18 December 1915':
            return 'S.S. Ruapehu 18 décembre 1915'
    return transport_reference
