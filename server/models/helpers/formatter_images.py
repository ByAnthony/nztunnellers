from typing import Optional
from models.helpers.translator_family import translate_family
from models.helpers.mapper_image_source_book_authors import map_authors


def get_image(url: str, source: dict) -> Optional[dict[str, str]]:
    if url is not None:
        return {'url': url, 'source': source}
    return None


def get_image_url(file: str) -> str:
    return file


def get_image_source(auckland_libraries: str, archives: dict, family: str, newspaper: dict, book: dict) -> dict:
    return {'auckland_libraries': auckland_libraries, 'archives': archives, 'family': family, 'newspaper': newspaper, 'book': book}


def get_image_source_auckland_libraries(reference: str) -> Optional[str]:
    if reference is not None:
        return '{}{}{}'.format('https://digitalnz.org/records?text=', reference, '&tab=Images#')
    return None


def get_image_source_archives(location: str, reference: str) -> Optional[dict[str, str]]:
    if location and reference is not None:
        return {'location': location, 'reference': reference}
    return None


def get_image_source_family(family: str, lang: str) -> Optional[str]:
    if family is not None:
        return translate_family(family, lang)
    return None


def get_image_source_newspaper(name: str, date: str) -> Optional[dict[str, str]]:
    if name and date is not None:
        return {'name': name, 'date': date}
    return None


def get_image_source_book(authors: tuple, title: str, town: str, publisher: str, year: str, page: str or None) -> Optional[dict]:
    if title is not None:
        return {'author': map_authors(authors), 'title': title, 'town': town, 'publisher': publisher, 'year': year, 'page': page}
    return None
