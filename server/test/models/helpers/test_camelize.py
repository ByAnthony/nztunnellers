# -*- coding: utf-8 -*-
from ....models.helpers.camelize_helpers import underscore_to_camel


class TestUnderscoreToCamel:
    def test_underscore_to_camel(self):
        assert (
            underscore_to_camel("{ pre_war_origin: { embarkation_unit: Main Body } }")
            == "{ preWarOrigin: { embarkationUnit: Main Body } }"
        )
