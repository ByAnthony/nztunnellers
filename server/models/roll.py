from dataclasses import dataclass


@dataclass
class Roll():
    id: int
    serial: str
    name: dict

    def get_name(forename: str, surname: str):
        return {'forename': forename, 'surname': surname}
