import json
from loaders.pokemon_loader import PokemonLoader

def test_load_all():

    bulba_data = {
        "bulbasaur": {
            "num": 1,
            "name": "Bulbasaur",
            "types": ["Grass", "Poison"],
            "genderRatio": {
                "M": 0.875,
                "F": 0.125
            },
            "baseStats": {
                "hp": 45,
                "atk": 49,
                "def": 49,
                "spa": 65,
                "spd": 65,
                "spe": 45
            },
            "abilities": {
                "0": "Overgrow",
                "H": "Chlorophyll"
            },
            "heightm": 0.7,
            "weightkg": 6.9,
            "color": "Green",
            "evos": [
                "Ivysaur"
            ],
            "eggGroups": [
                "Monster",
                "Grass"
            ]
        }
    }

    pl = PokemonLoader()

    assert pl.load_pokemon_by_id(1) == bulba_data