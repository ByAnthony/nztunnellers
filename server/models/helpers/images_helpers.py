from typing import Optional
from models.helpers.translator_helpers import translate_family
from models.image import Source, ImageArchives, ImageNewspaper, ImageBook, ImageBookAuthors


def get_image(url: str, source: dict) -> Optional[dict[str, str]]:
    if url is not None:
        return {'url': url, 'source': source}
    return None


def get_image_url(url: Optional[str]) -> Optional[str]:
    return url


def get_image_source(auckland_libraries: str, archives: dict, family: str, newspaper: dict, book: dict) -> Optional[Source]:
    if auckland_libraries is not None or archives is not None or family is not None or newspaper is not None or book is not None:
        return {'auckland_libraries': auckland_libraries, 'archives': archives, 'family': family, 'newspaper': newspaper, 'book': book}
    return None


def get_image_source_auckland_libraries(reference: Optional[str]) -> Optional[str]:
    if reference is not None:
        return '{}{}{}'.format('https://digitalnz.org/records?text=', reference, '&tab=Images#')
    return None


def get_image_source_archives(location: Optional[str], reference: Optional[str]) -> Optional[ImageArchives]:
    if location is not None and reference is not None:
        return {'location': location, 'reference': reference}
    return None


def get_image_source_family(family: Optional[str], lang: str) -> Optional[str]:
    if family is not None:
        return translate_family(family, lang)
    return None


def get_image_source_newspaper(name: Optional[str], date: Optional[str]) -> Optional[ImageNewspaper]:
    if name is not None and date is not None:
        return {'name': name, 'date': date}
    return None


def get_image_source_book(authors: list, title: Optional[str], town: Optional[str], publisher: Optional[str], year: Optional[str], page: Optional[str]) -> Optional[ImageBook]:
    def get_page(page: Optional[str]):
        if page is not None:
            no_break_space = '\N{NO-BREAK SPACE}'
            return 'p.{}{}'.format(no_break_space, page)
        return None

    if title is not None:
        return {'authors': map_authors(authors), 'title': title, 'town': town, 'publisher': publisher, 'year': year, 'page': get_page(page)}
    return None


def map_authors(authors: list) -> list[ImageBookAuthors]:
    return [{'forename': row['author_forename'], 'surname': row['author_surname']} for row in authors]
