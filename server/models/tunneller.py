import re
from dataclasses import dataclass
from datetime import date

from .roll import Roll
from .converter.month_year_converter import convert_month_year
from .formatter.date_formatter import assert_non_nullish_date_and_format, format_year
from .mapper.army_experience_mapper import map_army_experience
from .mapper.medals_mapper import map_medals
from .translator.transport_ref_translator import translate_transport_ref
from .translator.superscript_translator import translate_superscript


@dataclass
class Tunneller(Roll):
    origins: dict
    pre_war_life: dict
    military_life: dict

    def get_year(year: str, formatted_date: str):
        if year is not None:
            return year
        else:
            formatted_year = format_year(formatted_date)
            return formatted_year

    def get_date(date: date):
        return assert_non_nullish_date_and_format(date)

    def get_country(country: str):
        return country

    def get_town(town: str):
        return town

    def get_birth(
        birth_year: str,
        birth_date: str,
        birth_country: str
    ):
        return {
            'year': birth_year,
            'date': birth_date,
            'country': birth_country
        }

    def get_parent(name: str, origin_country: str):
        return {
            'name': name,
            'origin': origin_country
        }

    def get_nz_resident(in_nz_in_month: str, lang: str):
        return convert_month_year(in_nz_in_month, lang)

    def get_origins(
        birth: dict,
        mother: dict,
        father: dict,
        in_nz_length: str
    ):
        return {
            'birth': birth,
            'parents': {
                'mother': mother,
                'father': father
            },
            'in_nz_length': in_nz_length
        }

    def get_marital_status(status: str, wife_name: str):
        return {
            'status': status,
            'wife': wife_name
        }

    def get_occupation(occupation: str, employer: str):
        return {
            'name': occupation,
            'employer': employer
        }

    def get_religion(religion: str):
        return religion

    def get_army_experience(experience: tuple, lang: str):
        return map_army_experience(experience, lang)

    def get_pre_war_life(
        marital_status: dict,
        occupation: dict,
        residence: str,
        religion: str,
        army_experience: list
    ):
        return {
            'marital_status': marital_status,
            'occupation': occupation,
            'residence': residence,
            'religion': religion,
            'army_experience': army_experience
        }

    def get_alias(alias: str):
        return alias

    def get_military_district(military_district: str):
        return military_district

    def get_posted_from(posted_from: str):
        return posted_from

    def get_rank(rank: str):
        return rank

    def get_enlistment(
        enlistment_date: date,
        military_district: str,
        alias: str,
        posted_date: date,
        posted_from: str,
        rank: str,
    ):
        return {
            'enlistment_date': enlistment_date,
            'military_district': military_district,
            'alias': alias,
            'posted_date': posted_date,
            'posted_from': posted_from,
            'rank': rank
        }

    def get_transport_reference_uk(transport_reference: str, lang: str):
        return translate_transport_ref(transport_reference, lang)

    def get_vessel_uk(vessel: str):
        return vessel

    def get_transport_uk(
        transport_reference: str,
        vessel: str,
        departure_date: str,
        departure_port: str,
        arrival_date: str,
        arrival_port: str
    ):
        return {
            'transport_reference': transport_reference,
            'vessel': vessel,
            'departure_date': departure_date,
            'from': departure_port,
            'arrival_date': arrival_date,
            'to': arrival_port
        }

    def get_embarkation_unit_name(embarkation_unit_name: str, lang: str):
        return translate_superscript(embarkation_unit_name, lang)

    def get_section(section: str, lang: str):
        return translate_superscript(section, lang)

    def get_attached_corps(attached_corps: str):
        return attached_corps

    def get_embarkation_unit(
        embarkation_unit_name: str,
        section: str,
        attached_corps: str
    ):
        return {
            'embarkation_unit_name': embarkation_unit_name,
            'section': section,
            'attached_corps': attached_corps
        }

    def get_medals(medals: tuple):
        return map_medals(medals)

    def get_military_life(
        enlistment: dict,
        transport_uk: dict,
        embarkation_unit: dict,
        medals: list[dict]
    ):
        return {
            'enlistment': enlistment,
            'transport_uk': transport_uk,
            'embarkation_unit': embarkation_unit,
            'medals': medals
        }
