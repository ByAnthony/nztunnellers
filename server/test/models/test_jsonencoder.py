# -*- coding: utf-8 -*-
from dataclasses import dataclass
import json

from ...models.jsonencoder import JSONEncoder


@dataclass
class Person:
    name: str
    age: int


class TestJsonEncoderClass:
    def test_encoding(self):
        person = Person("Alice", 25)
        encoded_person = json.dumps(person, cls=JSONEncoder, indent=4)
        decoded_person = json.loads(encoded_person)

        assert encoded_person == '{\n    "name": "Alice",\n    "age": 25\n}'
        assert decoded_person["name"] == "Alice"
        assert decoded_person["age"] == 25

    def test_default(self):
        class MyEncoder(JSONEncoder):
            pass

        encoder = MyEncoder()
        obj = {"key": "value"}
        result = encoder.default(obj)
        assert result == str(obj)
