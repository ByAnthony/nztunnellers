def map_image(image, family, auckland_libraries):
    if (image is not None):
        if (family is not None):
            return {'file': image, 'source': {'family': '{} family'.format(family)}}
        if (auckland_libraries is not None):
            return {'file': image, 'source': {'auckland_libraries': auckland_libraries}}
