from typing import Optional
from models.sources import NewZealandArchives
from models.helpers.date_helpers import format_date
from models.sources import NominalRoll
from models.sources import LondonGazette


def map_nz_archives(nz_archives: list) -> list[NewZealandArchives]:
    link = 'https://collections.archives.govt.nz/web/arena/search#/item/aims-archive/R'
    return [{'reference': row['nz_archives_ref'], 'url': '{}{}'.format(link, row['nz_archives_url'])} for row in nz_archives]


def get_awmm(reference: str) -> str:
    return '{}{}'.format('https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/', reference)


def get_nominal_roll(volume: str, roll: str, page: str, lang: str) -> NominalRoll:

    no_break_space = '\N{NO-BREAK SPACE}'
    title_1919 = {'en': 'Nominal Rolls of New Zealand Expeditionary Force',
                  'fr': 'Liste nominative du corps expéditionnaire néo-zélandais'}
    title_1916 = {'en': 'Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company',
                  'fr': 'Liste nominative du corps expéditionnaire néo-zélandais, 1915. Compagnie de tunneliers'}
    roll_number_col = {'en': 'Roll No.', 'fr': 'Liste n\N{DEGREE SIGN}'}

    if volume and roll is not None:
        return {'title': title_1919[lang],
                'town': 'Wellington',
                'publisher': 'Government Printer',
                'date': '1914-1919',
                'volume': 'Volume{}{}'.format(no_break_space, volume),
                'roll': '{}{}{}'.format(roll_number_col[lang], no_break_space, roll),
                'page': 'p.{}{}'.format(no_break_space, page)}
    else:
        return {'title': title_1916[lang],
                'town': 'Wellington',
                'publisher': 'Government Printer',
                'date': '1916',
                'page': 'p.{}{}'.format(no_break_space, page)}


def map_london_gazette(london_gazette: list) -> list[Optional[LondonGazette]]:
    return [{'date': format_date(row['london_gazette_date']), 'page': row['london_gazette_page']} for row in london_gazette]
