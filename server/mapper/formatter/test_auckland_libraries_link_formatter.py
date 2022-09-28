from . import auckland_libraries_link_formatter


image_source = 'H-31 67829'


def test_if_source_is_not_none_returns_link():
    assert auckland_libraries_link_formatter.format_auckland_libraries_link(
        image_source) == '{}{}{}'.format('https://digitalnz.org/records?text=', image_source, '&tab=Images#')


def test_if_source_is_none_returns_none():
    assert auckland_libraries_link_formatter.format_auckland_libraries_link(
        None) == None
