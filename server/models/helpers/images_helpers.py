from typing import Optional
from models.helpers.translator_helpers import translate_family
from models.image import Image, Source, ImageArchives, ImageNewspaper, ImageBook, ImageBookAuthors


def get_image(url: str, source: Optional[Source]) -> Optional[Image]:
    if url is not None:
        return Image(url, source)
    return None


# To do: refactor when images are hosted
def get_image_url(url: str) -> str:
    return url


def get_image_source(auckland_libraries: Optional[str], archives: Optional[ImageArchives], family: Optional[str], newspaper: Optional[ImageNewspaper], book: Optional[ImageBook]) -> Optional[Source]:
    if auckland_libraries is not None or archives is not None or family is not None or newspaper is not None or book is not None:
        return Source(auckland_libraries, archives, family, newspaper, book)
    return None


def get_image_source_auckland_libraries(reference: Optional[str]) -> Optional[str]:
    if reference is not None:
        return '{}{}{}'.format('https://digitalnz.org/records?text=', reference, '&tab=Images#')
    return None


def get_image_source_archives(location: Optional[str], reference: Optional[str]) -> Optional[ImageArchives]:
    if location is not None and reference is not None:
        return ImageArchives(location, reference)
    return None


def get_image_source_family(family: str, lang: str) -> Optional[str]:
    if family is not None:
        return translate_family(family, lang)
    return None


def get_image_source_newspaper(name: str, date: str) -> Optional[ImageNewspaper]:
    if name is not None and date is not None:
        return ImageNewspaper(name, date)
    return None


def map_authors(authors: tuple[ImageBookAuthors]) -> list[ImageBookAuthors]:
    return [ImageBookAuthors(author['author_forename'], author['author_surname']) for author in authors]


def get_image_source_book(authors: tuple[ImageBookAuthors], title: Optional[str], town: Optional[str], publisher: Optional[str], year: Optional[str], page: Optional[str]) -> Optional[ImageBook]:
    def get_page(page: Optional[str]) -> Optional[str]:
        if page is not None:
            no_break_space = '\N{NO-BREAK SPACE}'
            return 'p.{}{}'.format(no_break_space, page)
        return None

    if title is not None and town is not None and publisher is not None and year is not None:
        return ImageBook(map_authors(authors), title, town, publisher, year, get_page(page))
    return None
