from ...models.roll import Name, Roll


name = Name("Anthony", "Byledbal")


class TestNameClass:
    def test_getitem(self):
        assert name["forename"] == "Anthony"
        assert name["surname"] == "Byledbal"


class TestRollClass:
    def test_getitem(self):
        roll = Roll(123, name, "1986", None)
        
        assert roll["id"] == 123
        assert roll["name"] == name
        assert roll["birth"] == "1986"
        assert roll["death"] is None
