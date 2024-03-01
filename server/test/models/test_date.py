from ...models.date import Date


class TestDateClass:
    def test_getitem(self):
        date = Date("2022", "02-25")

        assert date["year"] == "2022"
        assert date["day_month"] == "02-25"