def format_auckland_libraries_link(image_source):
    if image_source is not None:
        return '{}{}{}'.format('https://digitalnz.org/records?text=', image_source, '&tab=Images#')
    return None
