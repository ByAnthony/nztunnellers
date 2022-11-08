# -*- coding: utf-8 -*-
from ....models.helpers.image_helpers import map_authors
from ....models.image import ImageBookAuthors


author_1 = ImageBookAuthors("Arthur Conan", "Doyle")
author_2 = ImageBookAuthors("Mary", "Shelley")


def test_map_one_author():
    assert map_authors([author_1]) == [ImageBookAuthors("Arthur Conan", "Doyle")]


def test_map_multiple_authors():
    assert map_authors([author_1, author_2]) == [
        ImageBookAuthors("Arthur Conan", "Doyle"),
        ImageBookAuthors("Mary", "Shelley"),
    ]
