from datetime import date
from models.helpers.formatter_date import format_date


def get_training(start: date, location: str, location_type: str) -> dict[str, str, str]:
    return {'start': format_date(start), 'location': location, 'location_type': location_type}
