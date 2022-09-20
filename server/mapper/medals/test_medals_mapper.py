from . import medals_mapper


british_war_medal = {'medal_name': 'British War Medal',
                     'medal_citation': 'For bravery', 'country': 'United Kingdom'}
victory_medal = {'medal_name': 'Victory Medal',
                 'medal_citation': None, 'country': 'United Kingdom'}


def test_map_medals():
    assert medals_mapper.map_medals((british_war_medal, victory_medal)) == [
        {
            "citation":	"For bravery",
            "country": "United Kingdom",
            "name": "British War Medal"
        },
        {
            "citation":	None,
            "country": "United Kingdom",
            "name": "Victory Medal"
        }
    ]


def test_if_medals_do_not_exist_returns_empty_list():
    assert medals_mapper.map_medals(()) == []
