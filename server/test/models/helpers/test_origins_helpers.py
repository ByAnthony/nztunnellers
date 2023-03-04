# -*- coding: utf-8 -*-
from ....models.helpers.origins_helpers import get_nz_resident, get_parent
from ....models.origins import Parent


class TestGetParent:
    class TestGetParentIf:
        def test_name_and_origin_exist(self):
            assert get_parent("John Doe", "Scotland") == Parent("John Doe", "Scotland")

        def test_only_name_exists(self):
            assert get_parent("John Doe", None) == Parent("John Doe", None)

    class TestDoNotGetParentIf:
        def test_parent_does_not_exist(self):
            assert get_parent(None, None) is None


class TestGetNzResident:
    class TestGetNzResidentIf:
        def test_residence_is_less_than_12_months_returns_enlistment_year(self):
            assert get_nz_resident("5", "1916-09-29") == "1916"

        def test_residence_is_greater_than_12_months_returns_immigration_year(self):
            assert get_nz_resident("144", "1916-09-29") == "1904"

        def test_residence_is_null_returns_null(self):
            assert get_nz_resident(None, "1916-09-29") is None
