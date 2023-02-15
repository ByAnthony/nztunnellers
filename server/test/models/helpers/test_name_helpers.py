# -*- coding: utf-8 -*-
def set_surname_to_uppercase(surname: str):
    if surname.startswith("Mc"):
        return "Mc" + surname[2:].upper()
    return surname.upper()


class TestSetSurnameToUppercase:
    def test_set_surname_to_uppercase_if_name_starts_with_mc(self):
        assert set_surname_to_uppercase("McCow") == "McCOW"

    def test_don_not_set_surname_to_uppercase_if_name_does_not_start_with_mc(self):
        assert set_surname_to_uppercase("Beata") == "BEATA"
