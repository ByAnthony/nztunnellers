from dataclasses import dataclass
from typing import Optional
from models.helpers.transport_ref_translator import translate_transport_ref


@dataclass
class Transport:
    transport_reference: str
    vessel: str
    departure_date: str
    departure_port: Optional[str]
    arrival_date: Optional[str]
    arrival_port: Optional[str]

    def get_transport(transport_reference: str, vessel: str) -> dict[str, str, str, Optional[str], Optional[str], Optional[str]]:
        # if vessel and departure_date is not None:
        return {'transport_reference': transport_reference, 'vessel': vessel}
        # return None

    def get_transport_reference(transport_reference: str, lang: str) -> str:
        return translate_transport_ref(transport_reference, lang)

    # def get_transport(transport_reference: str, vessel: str, departure_date: str, departure_port: Optional[str], arrival_date: Optional[str], arrival_port: Optional[str]) -> dict[str, str, str, Optional[str], Optional[str], Optional[str]]:
    #     if vessel and departure_date is not None:
    #         return {'transport_reference': transport_reference, 'vessel': vessel, 'departure_date': departure_date, 'from': departure_port, 'arrival_date': arrival_date, 'to': arrival_port}
    #     return None
