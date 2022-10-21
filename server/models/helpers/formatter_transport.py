from models.helpers.translator_transport_ref import translate_transport_ref


def get_transport_reference(transport_reference: str, lang: str) -> str:
    return translate_transport_ref(transport_reference, lang)
