import re
from dataclasses import dataclass
from datetime import date
from .roll import Roll
from .converter.month_year_converter import convert_month_year
from .formatter.date_formatter import assert_non_nullish_date_and_format, format_year
from .mapper.army_experience_mapper import map_army_experience
from .mapper.medals_mapper import map_medals
from .translator.transport_ref_translator import translate_transport_ref


@dataclass
class Tunneller(Roll):
    origins: dict
    pre_war_life: dict
    military_life: dict

    def get_birth_year(birth_year: str, formatted_birth_date: str):
        if birth_year is not None:
            return birth_year
        else:
            formatted_year = format_year(formatted_birth_date)
            return formatted_year

    def get_birth_date(birth_date: date):
        return assert_non_nullish_date_and_format(birth_date)

    def get_birth_country(birth_country: str):
        return birth_country

    def get_birth_info(
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

    def get_residence(town: str):
        return town

    def get_religion(religion: str):
        return religion

    def get_army_experience(experience: list[dict], lang: str):
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

    def get_enlistment_date(enlistment_date: date):
        return assert_non_nullish_date_and_format(enlistment_date)

    def get_alias(alias: str):
        return alias

    def get_military_district(military_district: str):
        return military_district

    def get_posted_date(posted_date: date):
        return assert_non_nullish_date_and_format(posted_date)

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

    def get_departure_uk_date(departure_date: date):
        return assert_non_nullish_date_and_format(departure_date)

    def get_departure_uk_port(departure_port: str):
        return departure_port

    def get_arrival_uk_date(arrival_date: date):
        return assert_non_nullish_date_and_format(arrival_date)

    def get_arrival_uk_port(arrival_port: str):
        return arrival_port

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

    def get_medals(medals: list):
        return map_medals(medals)

    def get_military_life(
        enlistment: dict,
        transport_uk: dict,
        medals: list
    ):
        return {
            'enlistment': enlistment,
            'transport_uk': transport_uk,
            'medals': medals
        }
