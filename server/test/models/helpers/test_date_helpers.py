# -*- coding: utf-8 -*-
from ....models.date import Date
from ....models.helpers.date_helpers import (
    calculate_age_with_full_date,
    calculate_age_with_years,
    convert_immigration_duration_to_arrival_year,
    convert_month_in_duration,
    format_date_to_day,
    format_date_to_day_and_month,
    format_date_to_day_month_and_year,
    format_date_to_month,
    format_date_to_year,
    format_date_string_to_date_type,
    get_optional_date,
)

year = "1988"
date = "1988-05-04"
no_break_space = "\N{NO-BREAK SPACE}"


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
            assert format_date_to_month(None) is None


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
            assert (
                format_date_to_day_and_month("1962-09-27", "en")
                == f"27{no_break_space}September"
            )

        def test_lang_is_fr(self):
            assert (
                format_date_to_day_and_month("1962-06-23", "fr")
                == f"23{no_break_space}juin"
            )

    class TestDoNotFormatDateToDayAndMonthIf:
        def test_lang_is_en(self):
            assert format_date_to_day_and_month(None, "en") is None

        def test_lang_is_fr(self):
            assert format_date_to_day_and_month(None, "fr") is None


class TestFormatDateToDayMonthAndYear:
    class TestFormatDateToDayMonthAndYearIf:
        def test_lang_is_en(self):
            assert (
                format_date_to_day_month_and_year("1988-05-04", "en")
                == f"4{no_break_space}May 1988"
            )

        def test_lang_is_fr(self):
            assert (
                format_date_to_day_month_and_year("1986-01-26", "fr")
                == f"26{no_break_space}janvier 1986"
            )

    class TestDoNotFormatDateToDayMonthAndYearIf:
        def test_lang_is_en(self):
            assert format_date_to_day_month_and_year(None, "en") is None

        def test_lang_is_fr(self):
            assert format_date_to_day_month_and_year(None, "fr") is None


class TestGetBirthDate:
    def test_if_year_is_none_and_date_is_none_and_lang_is_en(self):
        assert format_date_string_to_date_type(None, None, "en") is None

    def test_if_year_is_none_and_date_is_none_and_lang_is_fr(self):
        assert format_date_string_to_date_type(None, None, "fr") is None

    def test_if_year_is_none_and_lang_is_en(self):
        assert format_date_string_to_date_type(None, date, "en") is None

    def test_if_year_is_none_and_lang_is_fr(self):
        assert format_date_string_to_date_type(None, date, "fr") is None

    def test_if_year_is_not_none_and_lang_is_en(self):
        assert format_date_string_to_date_type(year, None, "en") == Date("1988", None)

    def test_if_year_is_not_none_and_lang_is_fr(self):
        assert format_date_string_to_date_type(year, None, "fr") == Date("1988", None)


class TestGetDate:
    class TestGetDateIf:
        def test_lang_is_en(self):
            assert get_optional_date(date, "en") == Date(
                "1988", f"4{no_break_space}May"
            )

        def test_lang_is_fr(self):
            assert get_optional_date(date, "fr") == Date(
                "1988", f"4{no_break_space}mai"
            )

    class TestDoNotGetDateIf:
        def test_date_is_none_and_lang_is_en(self):
            assert get_optional_date(None, "en") is None

        def test_date_is_none_and_lang_is_fr(self):
            assert get_optional_date(None, "fr") is None


class TestConvertMonth:
    class TestConvertMonthIf:
        def test_month_is_equal_to_1_and_lang_en(self):
            assert convert_month_in_duration("1", "en") == f"1{no_break_space}month"

        def test_month_is_equal_to_1_and_lang_fr(self):
            assert convert_month_in_duration("1", "fr") == f"1{no_break_space}mois"

        def test_month_is_less_than_24_months_and_lang_en(self):
            assert convert_month_in_duration("15", "en") == f"15{no_break_space}months"

        def test_month_is_less_than_24_months_and_lang_fr(self):
            assert convert_month_in_duration("15", "fr") == f"15{no_break_space}mois"

        def test_month_is_more_than_24_months_and_lang_en(self):
            assert convert_month_in_duration("24", "en") == f"2{no_break_space}years"

        def test_month_is_more_than_24_months_and_lang_fr(self):
            assert convert_month_in_duration("250", "fr") == f"20{no_break_space}ans"

    class TestDoNotConvertMonthIf:
        def test_month_is_none_and_lang_en(self):
            assert convert_month_in_duration(None, "en") is None

        def test_month_is_none_and_lang_fr(self):
            assert convert_month_in_duration(None, "fr") is None


class TestConvertImmigrationYear:
    class TestConvertImmigrationYearIf:
        def test_residence_is_less_than_12_months_returns_enlistment_year(self):
            assert (
                convert_immigration_duration_to_arrival_year("5", "1916-09-29")
                == "1916"
            )

        def test_residence_is_greater_than_12_months_returns_immigration_year(self):
            assert (
                convert_immigration_duration_to_arrival_year("144", "1916-09-29")
                == "1904"
            )

        def test_residence_is_null_returns_null(self):
            assert (
                convert_immigration_duration_to_arrival_year(None, "1916-09-29") is None
            )


class TestCalculateAgeAtDeathWithFullDate:
    def test_calculate_age_with_full_date_with_year_minus_one(self):
        assert calculate_age_with_full_date("1876-07-14", "1962-06-06") == 85

    def test_calculate_age_with_full_date(self):
        assert calculate_age_with_full_date("1876-07-14", "1962-08-06") == 86


class TestCalculateAgeAtDeathWithYears:
    def calculate_age_with_years(self):
        assert calculate_age_with_years("1876", "1962") == 86
