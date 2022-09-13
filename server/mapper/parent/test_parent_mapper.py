from . import parent_mapper


def test_map_parent():
    assert parent_mapper.map_parent('John Williams', 'New Zeland') == {
        'name': 'John Williams', 'origin': 'New Zeland'}
