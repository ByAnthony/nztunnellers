# -*- coding: utf-8 -*-
from ....models.date import Date
from ....models.helpers.date_helpers import (
    convert_month_year,
    format_date_to_birth_year,
    format_date_to_day,
    format_date_to_day_and_month,
    format_date_to_day_month_and_year,
    format_date_to_month,
    format_date_to_year,
    get_birth_date,
    get_date,
)

no_break_space = "\N{NO-BREAK SPACE}"


def test_format_date_to_birth_year_if_full_date_exist():
    assert format_date_to_birth_year(None, "1988-05-04") == "1988"


def test_format_date_to_birth_year_if_year_exist():
    assert format_date_to_birth_year("1988", None) == "1988"


def test_do_not_format_date_to_birth_year_if_none_exist():
    assert format_date_to_birth_year(None, None) is None


def test_format_date_to_year_if_date_exists():
    assert format_date_to_year("1988-05-04") == "1988"


def test_do_not_format_date_to_year_if_date_does_not_exist():
    assert format_date_to_year(None) is None


def test_format_date_to_month_if_date_exists():
    assert format_date_to_month("1988-05-04") == "05"


def test_do_not_format_date_to_month_if_date_does_not_exist():
    assert format_date_to_month("1988-05-04") == "05"


def test_format_date_to_day_if_date_exists():
    assert format_date_to_day("1988-05-04") == "04"


def test_do_not_format_date_to_day_if_date_does_not_exist():
    assert format_date_to_day(None) is None


def test_format_date_to_day_and_month_if_lang_is_en():
    assert format_date_to_day_and_month("1962-09-27", "en") == "27{}September".format(
        no_break_space
    )


def test_format_date_to_day_and_month_if_lang_is_fr():
    assert format_date_to_day_and_month("1962-06-23", "fr") == "23{}juin".format(
        no_break_space
    )


def test_do_not_format_date_to_day_and_month_if_lang_is_en():
    assert format_date_to_day_and_month(None, "en") is None


def test_do_not_format_date_to_day_and_month_if_lang_is_fr():
    assert format_date_to_day_and_month(None, "fr") is None


def test_format_date_to_day_month_and_year_if_lang_is_en():
    assert format_date_to_day_month_and_year(
        "1988-05-04", "en"
    ) == "4{}May 1988".format(no_break_space)


def test_format_date_to_day_month_and_year_if_lang_is_fr():
    assert format_date_to_day_month_and_year(
        "1986-01-26", "fr"
    ) == "26{}janvier 1986".format(no_break_space)


def test_do_not_format_date_to_day_month_and_year_if_lang_is_en():
    assert format_date_to_day_month_and_year(None, "en") is None


def test_do_not_format_date_to_day_month_and_year_if_lang_is_fr():
    assert format_date_to_day_month_and_year(None, "fr") is None


year = "1988"
date = "1988-05-04"


def test_get_birth_date_if_year_is_none_and_lang_is_en():
    assert get_birth_date(None, date, "en") == Date(
        "1988", "4{}May".format(no_break_space)
    )


def test_get_birth_date_if_year_is_none_and_lang_is_fr():
    assert get_birth_date(None, date, "fr") == Date(
        "1988", "4{}mai".format(no_break_space)
    )


def test_get_birth_date_if_year_is_not_none_and_lang_is_en():
    assert get_birth_date(year, None, "en") == Date("1988", None)


def test_get_birth_date_if_year_is_not_none_and_lang_is_fr():
    assert get_birth_date(year, None, "fr") == Date("1988", None)


def test_get_date_if_lang_is_en():
    assert get_date(date, "en") == Date("1988", "4{}May".format(no_break_space))


def test_get_date_if_lang_is_fr():
    assert get_date(date, "fr") == Date("1988", "4{}mai".format(no_break_space))


def test_do_not_get_date_if_date_is_none_and_lang_is_en():
    assert get_date(None, "en") is None


def test_do_not_get_date_if_date_is_none_and_lang_is_fr():
    assert get_date(None, "fr") is None


def test_convert_month_year_if_month_is_equal_to_1_and_lang_en():
    assert convert_month_year("1", "en") == "1{}month".format(no_break_space)


def test_convert_month_year_if_month_is_equal_to_1_and_lang_fr():
    assert convert_month_year("1", "fr") == "1{}mois".format(no_break_space)


def test_convert_month_year_if_month_is_less_than_24_months_and_lang_en():
    assert convert_month_year("15", "en") == "15{}months".format(no_break_space)


def test_convert_month_year_if_month_is_less_than_24_months_and_lang_fr():
    assert convert_month_year("15", "fr") == "15{}mois".format(no_break_space)


def test_convert_month_year_if_month_is_more_than_24_months_and_lang_en():
    assert convert_month_year("24", "en") == "2{}years".format(no_break_space)


def test_convert_month_year_if_month_is_more_than_24_months_and_lang_fr():
    assert convert_month_year("250", "fr") == "20{}ans".format(no_break_space)


def test_do_not_convert_month_year_if_month_is_none_and_lang_en():
    assert convert_month_year(None, "en") is None


def test_do_not_convert_month_year_if_month_is_none_and_lang_fr():
    assert convert_month_year(None, "fr") is None
