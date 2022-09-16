def map_image(image, family, auckland_libraries, awmm_ref, awmm_title):
    return {'file': image, 'source': {'family': map_family(family), 'auckland_libraries': auckland_libraries, 'awmm': map_awmm(awmm_ref, awmm_title)}}


def map_awmm(ref, title):
    if ref is not None and title is None:
        return ref
    if ref is not None and title is not None:
        return '{}, {}'.format(ref, title)


def map_family(family):
    if (family is not None):
        return '{} family'.format(family)
