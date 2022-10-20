from dataclasses import dataclass
from datetime import date
from models.helpers.date_formatter import format_date


@dataclass
class Training:
    start: str
    location: str
    location_type: str

    def get_training(start: date, location: str, location_type: str) -> dict[str, str, str]:
        return {'start': format_date(start), 'location': location, 'location_type': location_type}
