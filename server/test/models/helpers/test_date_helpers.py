# -*- coding: utf-8 -*-
from ....models.date import Date
from ....models.helpers.date_helpers import (
    convert_immigration_year,
    convert_month_year,
    format_full_date_to_year,
    format_date_to_day,
    format_date_to_day_and_month,
    format_date_to_day_month_and_year,
    format_date_to_month,
    format_date_to_year,
    format_birth_and_death_date,
    get_optional_date,
)

year = "1988"
date = "1988-05-04"
no_break_space = "\N{NO-BREAK SPACE}"


class TestFormatDateBirth:
    class TestFormatDateBirthIf:
        def test_full_date_exist(self):
            assert format_full_date_to_year(None, "1988-05-04") == "1988"

        def test_only_year_exist(self):
            assert format_full_date_to_year("1988", None) == "1988"

    class TestDoNotFormatDateBirthIf:
        def test_date_does_not_exist(self):
            assert format_full_date_to_year(None, None) is None


class TestFormatDateToYear:
    class TestFormatDateToYearIf:
        def test_date_exists(self):
            assert format_date_to_year("1988-05-04") == "1988"

    class TestDoNotFormatDateToYearIf:
        def test_date_does_not_exist(self):
            assert format_date_to_year(None) is None


class TestFormatDateToMonth:
    class TestFormatDateToMonthIf:
        def test_date_exists(self):
            assert format_date_to_month("1988-05-04") == "05"

    class TestDoNotFormatDateToMonthIf:
        def test_do_not_format_date_to_month_if_date_does_not_exist(self):
            assert format_date_to_month("1988-05-04") == "05"


class TestFormatDateToDay:
    class TestFormatDateToDayIf:
        def test_date_exists(self):
            assert format_date_to_day("1988-05-04") == "04"

    class TestDoNotFormatDateToDayIf:
        def test_date_does_not_exist(self):
            assert format_date_to_day(None) is None


class TestFormatDateToDayAndMonth:
    class TestFormatDateToDayAndMonthIf:
        def test_lang_is_en(self):
            assert format_date_to_day_and_month(
                "1962-09-27", "en"
            ) == "27{}September".format(no_break_space)

        def test_lang_is_fr(self):
            assert format_date_to_day_and_month(
                "1962-06-23", "fr"
            ) == "23{}juin".format(no_break_space)

    class TestDoNotFormatDateToDayAndMonthIf:
        def test_lang_is_en(self):
            assert format_date_to_day_and_month(None, "en") is None

        def test_lang_is_fr(self):
            assert format_date_to_day_and_month(None, "fr") is None


class TestFormatDateToDayMonthAndYear:
    class TestFormatDateToDayMonthAndYearIf:
        def test_lang_is_en(self):
            assert format_date_to_day_month_and_year(
                "1988-05-04", "en"
            ) == "4{}May 1988".format(no_break_space)

        def test_lang_is_fr(self):
            assert format_date_to_day_month_and_year(
                "1986-01-26", "fr"
            ) == "26{}janvier 1986".format(no_break_space)

    class TestDoNotFormatDateToDayMonthAndYearIf:
        def test_lang_is_en(self):
            assert format_date_to_day_month_and_year(None, "en") is None

        def test_lang_is_fr(self):
            assert format_date_to_day_month_and_year(None, "fr") is None


class TestGetBirthDate:
    def test_if_year_is_none_and_lang_is_en(self):
        assert format_birth_and_death_date(None, date, "en") == Date(
            "1988", "4{}May".format(no_break_space)
        )

    def test_if_year_is_none_and_lang_is_fr(self):
        assert format_birth_and_death_date(None, date, "fr") == Date(
            "1988", "4{}mai".format(no_break_space)
        )

    def test_if_year_is_not_none_and_lang_is_en(self):
        assert format_birth_and_death_date(year, None, "en") == Date("1988", None)

    def test_if_year_is_not_none_and_lang_is_fr(self):
        assert format_birth_and_death_date(year, None, "fr") == Date("1988", None)


class TestGetDate:
    class TestGetDateIf:
        def test_lang_is_en(self):
            assert get_optional_date(date, "en") == Date(
                "1988", "4{}May".format(no_break_space)
            )

        def test_lang_is_fr(self):
            assert get_optional_date(date, "fr") == Date(
                "1988", "4{}mai".format(no_break_space)
            )

    class TestDoNotGetDateIf:
        def test_date_is_none_and_lang_is_en(self):
            assert get_optional_date(None, "en") is None

        def test_date_is_none_and_lang_is_fr(self):
            assert get_optional_date(None, "fr") is None


class TestConvertMonth:
    class TestConvertMonthIf:
        def test_month_is_equal_to_1_and_lang_en(self):
            assert convert_month_year("1", "en") == "1{}month".format(no_break_space)

        def test_month_is_equal_to_1_and_lang_fr(self):
            assert convert_month_year("1", "fr") == "1{}mois".format(no_break_space)

        def test_month_is_less_than_24_months_and_lang_en(self):
            assert convert_month_year("15", "en") == "15{}months".format(no_break_space)

        def test_month_is_less_than_24_months_and_lang_fr(self):
            assert convert_month_year("15", "fr") == "15{}mois".format(no_break_space)

        def test_month_is_more_than_24_months_and_lang_en(self):
            assert convert_month_year("24", "en") == "2{}years".format(no_break_space)

        def test_month_is_more_than_24_months_and_lang_fr(self):
            assert convert_month_year("250", "fr") == "20{}ans".format(no_break_space)

    class TestDoNotConvertMonthIf:
        def test_month_is_none_and_lang_en(self):
            assert convert_month_year(None, "en") is None

        def test_month_is_none_and_lang_fr(self):
            assert convert_month_year(None, "fr") is None


class TestConvertImmigrationYear:
    class TestConvertImmigrationYearIf:
        def test_residence_is_less_than_12_months_returns_enlistment_year(self):
            assert convert_immigration_year("5", "1916-09-29") == "1916"

        def test_residence_is_greater_than_12_months_returns_immigration_year(self):
            assert convert_immigration_year("144", "1916-09-29") == "1904"

        def test_residence_is_null_returns_null(self):
            assert convert_immigration_year(None, "1916-09-29") is None
