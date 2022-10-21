from models.helpers.mapper_nz_archives import map_nz_archives
from models.helpers.formatter_nominal_roll import format_nominal_roll
from models.helpers.mapper_london_gazette import map_london_gazette


def get_sources(nz_archives: str, awmm: str, nominal_roll: str, london_gazette: list[dict]) -> dict:
    return {'nz_archives': nz_archives, 'awmm': awmm, 'nominal_roll': nominal_roll, 'london_gazette': london_gazette}


def get_nz_archives(reference: tuple) -> list[dict]:
    return map_nz_archives(reference)


def get_awmm(reference: str) -> str:
    return '{}{}'.format('https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/', reference)


def get_nominal_roll(volume: str, roll: str, page: str, lang: str) -> dict:
    return format_nominal_roll(volume, roll, page, lang)


def get_london_gazette(reference: tuple) -> dict:
    return map_london_gazette(reference)
