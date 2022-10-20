from dataclasses import dataclass


@dataclass
class Name:
    forename: str
    surname: str

    def get_name(forename: str, surname: str) -> dict[str, str]:
        return {'forename': forename, 'surname': surname}
