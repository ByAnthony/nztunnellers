# -*- coding: utf-8 -*-
# from ....models.helpers import month_year_converter
# from ....models.mapper import army_experience_mapper

# country_col = {"en": "New Zealand", "fr": "Nouvelle-Zélande"}
# conflict_col = {"en": "South African War", "fr": "Guerre d'Afrique du Sud"}

# experience_en = (
#     {
#         "army_experience_name": "Garrison Artillery Volunteers",
#         "country": "New Zealand",
#         "conflict_name": None,
#         "army_experience_in_month": 12,
#     },
#     {
#         "army_experience_name": None,
#         "country": None,
#         "conflict_name": "South African War",
#         "army_experience_in_month": 250,
#     },
# )
# experience_fr = (
#     {
#         "army_experience_name": "National Reserve",
#         "country": "Nouvelle-Zélande",
#         "conflict_name": "Guerre d'Afrique du Sud",
#         "army_experience_in_month": 50,
#     },
# )


# def test_map_army_experience_in_english():
#     assert army_experience_mapper.map_army_experience(experience_en, "en") == [
#         {
#             "unit": "Garrison Artillery Volunteers",
#             "country": country_col["en"],
#             "conflict": None,
#             "duration": month_year_converter.convert_month_year(12, "en"),
#         },
#         {
#             "unit": None,
#             "country": None,
#             "conflict": "South African War",
#             "duration": month_year_converter.convert_month_year(250, "en"),
#         },
#     ]


# def test_map_army_experience_in_french():
#     assert army_experience_mapper.map_army_experience(experience_fr, "fr") == [
#         {
#             "unit": "National Reserve",
#             "country": country_col["fr"],
#             "conflict": "Guerre d'Afrique du Sud",
#             "duration": month_year_converter.convert_month_year(50, "fr"),
#         }
#     ]
