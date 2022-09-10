def map_nz_archives(ref_1, url_1, ref_2, url_2):
    if (ref_2 is not None and url_2 is not None):
        return [
            {'ref': ref_1, 'url': url_1},
            {'ref': ref_2, 'url': url_2}
        ]
    return [
        {'ref': ref_1, 'url': url_1}
    ]
