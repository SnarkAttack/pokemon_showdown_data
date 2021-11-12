from loaders.ability_loader import AbilityLoader

def test_ability_loader():

    adaptability_data = {
		"name": "Adaptability",
		"rating": 4,
		"num": 91,
	}

    al = AbilityLoader()

    assert al.load_ability_by_key('adaptability') == adaptability_data