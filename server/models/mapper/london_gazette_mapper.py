from ..formatter.date_formatter import format_date


def map_london_gazette(london_gazette: tuple) -> list[dict]:
    return [{'date': format_date(row['london_gazette_date']),
            'page': row['london_gazette_page']} for row in london_gazette]
