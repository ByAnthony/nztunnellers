from dataclasses import dataclass


@dataclass
class Roll():
    id: int
    serial: str
    name: dict

    def get_id(id: int) -> int:
        return id

    def get_serial(serial: str) -> str:
        return serial

    def get_name(forename: str, surname: str) -> dict:
        return {'forename': forename, 'surname': surname}
