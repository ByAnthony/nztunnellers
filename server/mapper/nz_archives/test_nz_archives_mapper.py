from . import nz_archives_mapper

actual_ref_1 = {'nz_archives_ref': 'AABK 18805 W5520 1/0006561',
                'nz_archives_url': '22280535'}
actual_ref_2 = {'nz_archives_ref': 'AABK 18805 W5520 1/0006563',
                'nz_archives_url': '22280537'}

expected_ref_1 = {"reference": "AABK 18805 W5520 1/0006561", "url": "22280535"}
expected_ref_2 = {"reference": "AABK 18805 W5520 1/0006563", "url": "22280537"}


def test_if_archives_has_one_record():
    assert nz_archives_mapper.map_nz_archives((actual_ref_1,)) == [
        expected_ref_1
    ]


def test_if_archives_has_two_records():
    assert nz_archives_mapper.map_nz_archives((actual_ref_1, actual_ref_2)) == [
        expected_ref_1,
        expected_ref_2,
    ]
