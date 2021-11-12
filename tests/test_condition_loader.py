from loaders import ConditionLoader

def test_condition_loader():

    sandstorm_data = {
		"name": 'Sandstorm',
		"effectType": 'Weather',
		"duration": 5,
        "onModifySpDPriority": 10,
		"onFieldResidualOrder": 1,
	}

    cl = ConditionLoader()

    print(cl.load_condition_by_key('sandstorm'))

    assert cl.load_condition_by_key('sandstorm') == sandstorm_data