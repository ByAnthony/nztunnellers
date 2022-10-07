from dataclasses import dataclass


@dataclass
class Roll():
    id: int
    name: dict
    serial: str

    def get_name(forename: str, surname: str):
        return {"forename": forename, "surname": surname}
