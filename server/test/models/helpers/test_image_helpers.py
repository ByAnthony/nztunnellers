# -*- coding: utf-8 -*-
from ....models.helpers.image_helpers import (
    get_image,
    get_image_source,
    get_image_source_archives,
    get_image_source_auckland_libraries,
    get_image_source_book,
    get_image_source_family,
    get_image_source_newspaper,
    get_image_url,
    map_authors,
)
from ....models.image import (
    Image,
    ImageArchives,
    ImageBook,
    ImageBookAuthors,
    ImageNewspaper,
    Source,
)

author_1 = ImageBookAuthors("Arthur Conan", "Doyle")
author_2 = ImageBookAuthors("Mary", "Shelley")

no_break_space = "\N{NO-BREAK SPACE}"

image_auckland_libraries = "{}{}{}".format(
    "https://digitalnz.org/records?text=", "fake_reference", "&tab=Images#"
)
image_archives = ImageArchives("Archives New Zealand", "fake_reference")
family = "Doe"
image_newspaper = ImageNewspaper("Auckland Weekly News", "4 May 1888")
image_book = ImageBook([author_1], "A Study In Red", "London", "Penguins", "1962", "2")


class TestGetImage:
    def test_if_url_and_source_exist(self):
        assert get_image(
            "https://www.nztunnellers.com/photo",
            Source(image_auckland_libraries, None, None, None, None),
        ) == Image(
            "https://www.nztunnellers.com/photo",
            Source(image_auckland_libraries, None, None, None, None),
        )

    def test_if_url_exists(self):
        assert get_image("https://www.nztunnellers.com/photo", None) == Image(
            "https://www.nztunnellers.com/photo", None
        )

    def test_if_image_and_url_do_not_exist(self):
        assert get_image(None, None) is None


class TestGetImageUrl:
    # TODO: refactor when images are hosted
    def test_if_url_exists(self):
        assert (
            get_image_url("https://www.nztunnellers.com/photo")
            == "https://www.nztunnellers.com/photo"
        )

    # TODO: refactor when images are hosted
    def test_if_url_does_not_exist(self):
        assert get_image_url(None) is None


class TestGetImageSource:
    def test_if_auckland_libraries_exist(self):
        assert get_image_source(
            image_auckland_libraries, None, None, None, None
        ) == Source(image_auckland_libraries, None, None, None, None)

    def test_if_archives_exist(self):
        assert get_image_source(None, image_archives, None, None, None) == Source(
            None, image_archives, None, None, None
        )

    def test_if_family_exists(self):
        assert get_image_source(None, None, family, None, None) == Source(
            None, None, family, None, None
        )

    def test_if_newspaper_exists(self):
        assert get_image_source(None, None, None, image_newspaper, None) == Source(
            None, None, None, image_newspaper, None
        )

    def test_if_book_exists(self):
        assert get_image_source(None, None, None, None, image_book) == Source(
            None, None, None, None, image_book
        )

    def test_if_no_images_exist(self):
        assert get_image_source(None, None, None, None, None) is None


class TestGetImageSourceAucklandLibraries:
    def test_if_reference_exists(self):
        assert get_image_source_auckland_libraries("fake_reference") == "{}{}{}".format(
            "https://digitalnz.org/records?text=", "fake_reference", "&tab=Images#"
        )

    def test_if_reference_does_not_exist(self):
        assert get_image_source_auckland_libraries(None) is None


class TestGetImageSourceArchives:
    def test_if_archives_exist(self):
        assert get_image_source_archives(
            "Archives New Zealand", "fake_reference"
        ) == ImageArchives("Archives New Zealand", "fake_reference")

    def test_if_archives_do_not_exist(self):
        assert get_image_source_archives(None, None) is None


class TestGetImageSourceFamily:
    class TestGetImageSourceFamilyIf:
        def test_family_exists_and_lang_is_en(self):
            assert get_image_source_family("Doe", "en") == "Doe family"

        def test_family_exists_and_lang_is_fr(self):
            assert get_image_source_family("Doe", "fr") == "Famille Doe"

    class TestDoNotGetImageSourceFamilyIf:
        def test_family_does_not_exist_and_lang_is_en(self):
            assert get_image_source_family(None, "en") is None

        def test_family_does_not_exist_and_lang_is_fr(self):
            assert get_image_source_family(None, "fr") is None


class TestGetImageSourceNewspaper:
    def test_if_newspaper_exist(self):
        assert get_image_source_newspaper(
            "Auckland Weekly News", "4 May 1888"
        ) == ImageNewspaper("Auckland Weekly News", "4 May 1888")

    def test_if_newspaper_does_not_exist(self):
        assert get_image_source_newspaper(None, None) is None


class TestMapAuthors:
    class TestMapAuthorsIf:
        def test_one_author(self):
            assert map_authors([author_1]) == [
                ImageBookAuthors("Arthur Conan", "Doyle")
            ]

        def test_multiple_authors(self):
            assert map_authors([author_1, author_2]) == [
                ImageBookAuthors("Arthur Conan", "Doyle"),
                ImageBookAuthors("Mary", "Shelley"),
            ]

    class TestDoNotMapAuthorsIf:
        def test_empty_list(self):
            assert map_authors([]) == []


class TestGetImageSourceBook:
    def test_with_page(self):
        assert get_image_source_book(
            [author_1], "A Study In Red", "London", "Penguins", "1962", "2"
        ) == ImageBook(
            [author_1],
            "A Study In Red",
            "London",
            "Penguins",
            "1962",
            "p.{}{}".format(no_break_space, "2"),
        )

    def test_with_no_page(self):
        assert get_image_source_book(
            [author_1, author_2], "A Study In Red", "London", "Penguins", "1962", None
        ) == ImageBook(
            [author_1, author_2], "A Study In Red", "London", "Penguins", "1962", None
        )

    def test_when_no_source_book(self):
        assert get_image_source_book(
            [author_1, author_2], None, None, None, None, None
        ) is None
