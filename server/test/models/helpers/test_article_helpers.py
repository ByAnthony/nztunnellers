# -*- coding: utf-8 -*-
from ....db.models.ArticleData import (
    ArticleReferenceData,
    FileData,
    ImageData,
    SectionData,
)
from ....models.article import Image, Next, Section
from ....models.helpers.article_helpers import (
    get_images,
    get_next_chapter,
    map_images,
    map_sections,
)


class TestGetImages:
    def test_get_images(self):
        mocked_file_data_list = (
            FileData("image-1"),
            FileData("image-2"),
            FileData("image-3"),
        )

        assert get_images(mocked_file_data_list, 0) == "image-1"
        assert get_images(mocked_file_data_list, 1) == "image-2"
        assert get_images(mocked_file_data_list, 2) == "image-3"
        assert get_images(mocked_file_data_list, 3) == ""


class TestGetNextChapter:
    def test_get_next_chapter(self):
        mocked_article_reference_data_list = (
            ArticleReferenceData("title-test-1", 1, "Title Test 1"),
            ArticleReferenceData("title-test-2", 2, "Title Test 2"),
            ArticleReferenceData("title-test-3", 3, "Title Test 3"),
        )

        assert get_next_chapter(1, mocked_article_reference_data_list) == Next(
            "title-test-2", 2, "Title Test 2"
        )
        assert get_next_chapter(2, mocked_article_reference_data_list) == Next(
            "title-test-3", 3, "Title Test 3"
        )
        assert get_next_chapter(3, mocked_article_reference_data_list) is None

    def test_get_next_chapter_when_empty_list(self):
        assert get_next_chapter(0, ()) is None


class TestMapSections:
    def test_map_sections(self):
        mocked_section_data_list = (
            SectionData("Title", "a very long text"),
            SectionData("Title 2", "a very very long text"),
        )

        assert map_sections(mocked_section_data_list) == [
            Section("Title", "a very long text"),
            Section("Title 2", "a very very long text"),
        ]


class TestMapImages:
    def test_map_images(self):
        mocked_image_data_list = (
            ImageData("image-1.jpg", None, None, None, "Alt text for image-1"),
            ImageData(
                "image-2.jpg",
                "Image 2 title",
                "Photographer",
                "Reference",
                "Alt text for image-2",
            ),
            ImageData(
                "image-3.jpg",
                "Image 3 title",
                "Photographer",
                "Reference",
                "Alt text for image-3",
            ),
        )

        assert map_images(mocked_image_data_list) == [
            Image("image-1.jpg", None, None, None, "Alt text for image-1"),
            Image(
                "image-2.jpg",
                "Image 2 title",
                "Photographer",
                "Reference",
                "Alt text for image-2",
            ),
            Image(
                "image-3.jpg",
                "Image 3 title",
                "Photographer",
                "Reference",
                "Alt text for image-3",
            ),
        ]
