# -*- coding: utf-8 -*-
from ...models.post_service_years import PostServiceYears
from ...models.sources import Sources
from ...models.military_years import MilitaryYears
from ...models.pre_war_years import PreWarYear
from ...models.origins import Origins
from ...models.summary import Summary
from ...models.tunneller import Tunneller
from unittest.mock import Mock

mocked_summary = Mock(spec=Summary)
mocked_origins = Mock(spec=Origins)
mocked_pre_war_years = Mock(spec=PreWarYear)
mocked_military_years = Mock(spec=MilitaryYears)
mocked_post_service_years = Mock(spec=PostServiceYears)
mocked_sources = Mock(spec=Sources)


class TestTunnellerClass:
    def test_getitem(self):
        tunneller: Tunneller = Tunneller(
            123,
            mocked_summary,
            mocked_origins,
            mocked_pre_war_years,
            mocked_military_years,
            mocked_post_service_years,
            mocked_sources,
            None,
        )

        assert tunneller["id"] == 123
        assert tunneller["summary"] == mocked_summary
        assert tunneller["origins"] == mocked_origins
        assert tunneller["pre_war_years"] == mocked_pre_war_years
        assert tunneller["military_years"] == mocked_military_years
        assert tunneller["post_service_years"] == mocked_post_service_years
        assert tunneller["sources"] == mocked_sources
