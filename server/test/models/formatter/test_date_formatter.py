# -*- coding: utf-8 -*-
from datetime import date

from server.models.helpers import date_helpers


def test_format_date_to_return_Y_m_d():
    assert date_helpers.format_date(date(1886, 1, 26)) == "1886-01-26"


def test_format_year():
    assert date_helpers.format_year("1886-01-26") == "1886"
