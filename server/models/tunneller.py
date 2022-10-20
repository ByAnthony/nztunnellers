import re
from dataclasses import dataclass

from .roll import Roll
from .origins import Origins
from .converter.month_year_converter import convert_month_year
from .formatter.date_formatter import format_date, format_year
from .formatter.nominal_roll_formatter import format_nominal_roll
from .mapper.army_experience_mapper import map_army_experience
from .mapper.image_source_book_authors_mapper import map_authors
from .mapper.london_gazette_mapper import map_london_gazette
from .mapper.medals_mapper import map_medals
from .mapper.nz_archives_mapper import map_nz_archives
from .translator.family_translator import translate_family
from .translator.has_deserted_translator import translate_has_deserted
from .translator.superscript_translator import translate_superscript
from .translator.transport_ref_translator import translate_transport_ref


@dataclass
class Tunneller(Roll):
    origins: Origins

    # pre_war_years: dict[str, str, dict[str, str],
    #                     str, str, list[dict[str, str, str, str]]]
    # military_years: dict
    # image: dict or None
    # sources: dict

    # def get_origins(birth_details: dict[str, str, str], parents: dict[dict[str, str], dict[str, str]], in_nz_length: str) -> dict[dict[str, str, str], dict[dict[str, str], dict[str, str]], str]:
    #     return {'birth': birth_details, 'parents': parents, 'in_nz_length': in_nz_length}

    # def get_birth_details(year: str or None, date: date or None, country: str or None) -> dict[str, str, str]:
    #     birth_date = format_date(date)
    #     birth_year = get_year(year, birth_date)
    #     birth_country = get_country(country)
    #     return {'year': birth_year, 'date': birth_date, 'country': birth_country}

    # def get_parents(mother: dict[str, str], father: dict[str, str]) -> dict[dict[str, str], dict[str, str]]:
    #     return {'mother': mother, 'father': father}

    # def get_parent(name: str or None, country: str or None) -> dict[str, str]:
    #     parent_name = get_name(name)
    #     origin_country = get_country(country)
    #     return {'name': parent_name, 'origin': origin_country}

    # def get_nz_resident(in_nz_in_month: str or None, lang: str) -> str:
    #     if in_nz_in_month is not None:
    #         return convert_month_year(in_nz_in_month, lang)

    # def get_pre_war_years(marital_status: Optional[str], wife: str or None, employment: dict[str, str], residence: str or None, religion: str or None, army_experience: list[dict[str, str, str, str]]) -> dict[str, str, dict[str, str], str, str, list[dict[str, str, str, str]]]:
    #     def get_marital_status(status: str or None) -> str:
    #         if status is not None:
    #             return status

    #     def get_religion(religion: str or None) -> str:
    #         if religion is not None:
    #             return religion
    #     return {'marital_status': get_marital_status(marital_status), 'wife': get_name(wife), 'employment': employment, 'residence': get_town(residence), 'religion': get_religion(religion), 'army_experience': army_experience}

    # def get_employment(occupation: str, employer: str or None) -> dict[str, str]:
    #     def get_occupation(occupation: str) -> str:
    #         return occupation

    #     def get_employer(employer: str or None) -> str:
    #         if employer is not None:
    #             return employer
    #     return {'occupation': get_occupation(occupation), 'employer': get_employer(employer)}

    # def get_army_experience(experience: tuple, lang: str) -> list[dict[str, str, str, str]]:
    #     return map_army_experience(experience, lang)

    # def get_military_years(enlistment: dict, embarkation_unit: dict, transport_uk: dict, transport_nz: dict, end_of_service: dict, medals: list[dict]) -> dict:
    #     return {'enlistment': enlistment, 'embarkation_unit': embarkation_unit, 'transport_uk': transport_uk, 'transport_nz': transport_nz, 'end_of_service': end_of_service, 'medals': medals}

    # def get_military_years(enlistment: dict) -> dict:
    #     return {'enlistment': enlistment}

    # def get_enlistment(enlistment_date: date or None, military_district: str or None, alias: str or None, transferred_to_tunnellers: dict[str, str], rank: str) -> dict:
    #     def get_military_district(military_district: str or None) -> str:
    #         if military_district is not None:
    #             return military_district

    #     def get_alias(alias: str or None) -> str:
    #         if alias is not None:
    #             return alias
    #     return {'enlistment_date': format_date(enlistment_date), 'military_district': get_military_district(military_district), 'alias': get_alias(alias), 'transferred_to_tunnellers': transferred_to_tunnellers, 'rank': rank}

    # def get_transferred_to_tunnellers(posted_date: date or None, posted_from: str or None) -> dict[str, str]:
    #     if posted_date and posted_from is not None:
    #         return {'posted_date': posted_date, 'posted_from': posted_from}

    # def get_posted_from(posted_from: str):
    #     return posted_from

    # def get_rank(rank: str) -> str:
    #     return rank

    # def get_embarkation_unit(detachment: str, section: str, attached_corps: str, training: dict) -> dict:
    #     return {'detachment': detachment, 'section': section, 'attached_corps': attached_corps, 'training': training}

    # def get_detachment(detachment: str, lang: str):
    #     return translate_superscript(detachment, lang)

    # def get_section(section: str, lang: str) -> str:
    #     return translate_superscript(section, lang)

    # def get_attached_corps(attached_corps: str) -> str:
    #     return attached_corps

    # def get_training(start: date, location: str, location_type: str) -> dict:
    #     return {'start': start, 'location': location, 'location_type': location_type}

    # def get_training_location(location: str) -> str:
    #     return location

    # def get_training_location_type(type: str) -> str:
    #     return type

    # def get_transport(transport_reference: str, vessel: str, departure_date: str, departure_port: str, arrival_date: str, arrival_port: str) -> dict:
    #     if vessel and departure_date is not None:
    #         return {'transport_reference': transport_reference, 'vessel': vessel, 'departure_date': departure_date, 'from': departure_port, 'arrival_date': arrival_date, 'to': arrival_port}
    #     return None

    # def get_transport_reference(transport_reference: str, lang: str) -> str:
    #     return translate_transport_ref(transport_reference, lang)

    # def get_vessel(vessel: str) -> str:
    #     return vessel

    # def get_end_of_service(has_deserted: str or None) -> dict:
    #     if has_deserted is not None:
    #         return {'deserter': {'text': has_deserted}}
    #     return {'deserter': None}

    # def get_end_of_service_as_deserter(value: bool or None, lang: str) -> str or None:
    #     return translate_has_deserted(value, lang)

    # def get_medals(medals: tuple) -> list[dict]:
    #     return map_medals(medals)

    # def get_image(url: str, source: dict) -> dict or None:
    #     if url is not None:
    #         return {'url': url, 'source': source}
    #     return None

    # def get_image_url(file: str) -> str:
    #     return file

    # def get_image_source(auckland_libraries: str, archives: dict, family: str, newspaper: dict, book: dict) -> dict:
    #     return {'auckland_libraries': auckland_libraries, 'archives': archives, 'family': family, 'newspaper': newspaper, 'book': book}

    # def get_image_source_auckland_libraries(reference: str) -> str or None:
    #     if reference is not None:
    #         return '{}{}{}'.format('https://digitalnz.org/records?text=', reference, '&tab=Images#')
    #     return None

    # def get_image_source_archives(location: str, reference: str) -> dict or None:
    #     if location and reference is not None:
    #         return {'location': location, 'reference': reference}
    #     return None

    # def get_image_source_family(family: str, lang: str) -> str or None:
    #     if family is not None:
    #         return translate_family(family, lang)
    #     return None

    # def get_image_source_newspaper(name: str, date: date) -> dict or None:
    #     if name and date is not None:
    #         return {'name': name, 'date': date}
    #     return None

    # def get_image_source_book(authors: tuple, title: str, town: str, publisher: str, year: str, page: str or None) -> dict or None:
    #     if title is not None:
    #         return {'author': map_authors(authors), 'title': title, 'town': town, 'publisher': publisher, 'year': year, 'page': page}
    #     return None

    # def get_sources(nz_archives: str, awmm: str, nominal_roll: str, london_gazette: list[dict]) -> dict:
    #     return {'nz_archives': nz_archives, 'awmm': awmm, 'nominal_roll': nominal_roll, 'london_gazette': london_gazette}

    # def get_nz_archives(reference: tuple) -> list[dict]:
    #     return map_nz_archives(reference)

    # def get_awmm(reference: str) -> str:
    #     return '{}{}'.format('https://www.aucklandmuseum.com/war-memorial/online-cenotaph/record/', reference)

    # def get_nominal_roll(volume: str, roll: str, page: str, lang: str) -> dict:
    #     return format_nominal_roll(volume, roll, page, lang)

    # def get_london_gazette(reference: tuple) -> dict:
    #     return map_london_gazette(reference)
