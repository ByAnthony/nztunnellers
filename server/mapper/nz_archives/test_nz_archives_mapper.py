from . import nz_archives_mapper

ref_1 = 'AABK 18805'
url_1 = '7834729'
ref_2 = 'AABK 18806'
url_2 = '5645327'


def test_if_archives_ref_2_and_url_2_is_not_none():
    assert nz_archives_mapper.map_nz_archives(ref_1, url_1, ref_2, url_2) == [
        {'ref': ref_1, 'url': url_1},
        {'ref': ref_2, 'url': url_2}
    ]


def test_if_archives_ref_2_and_url_2_is_none():
    assert nz_archives_mapper.map_nz_archives(ref_1, url_1, None, None) == [
        {'ref': ref_1, 'url': url_1}
    ]
