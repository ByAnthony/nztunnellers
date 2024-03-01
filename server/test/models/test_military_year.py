
from ...models.date import Date
from ...models.military_years import Event, EventDetails, Events, SingleEvent


battlefield_event_details = EventDetails("Frontline", "Battle", "image.jpg")

class TestEventDetailsClass:
    def test_getitem(self):
        assert battlefield_event_details["description"] == "Frontline"
        assert battlefield_event_details["title"] == "Battle"
        assert battlefield_event_details["image"] == "image.jpg"


class TestEventsClass:
    def test_getitem(self):
        events = Events(Date("1916", "04-16"), [battlefield_event_details, battlefield_event_details])

        assert events["date"] == Date("1916", "04-16")
        assert events["event"] == [battlefield_event_details, battlefield_event_details]


class TestEventClass:
    def test_getitem(self):
        event = Event(Date("1916", "04-16"), battlefield_event_details)

        assert event["date"] == Date("1916", "04-16")
        assert event["event"] == battlefield_event_details


class TestSingleEventClass:
    def test_getitem(self):
        single_event = SingleEvent(Date("1916", "04-16"), "Frontline", "Battle", "image.jpg")

        assert single_event["date"] == Date("1916", "04-16")
        assert single_event["event"] == "Frontline"
        assert battlefield_event_details["title"] == "Battle"
        assert battlefield_event_details["image"] == "image.jpg"
