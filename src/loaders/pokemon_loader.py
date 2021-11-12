from .base_loader import BaseLoader

class PokemonLoader(BaseLoader):

    def __init__(self):
        super().__init__('pokedex.ts')

    def load_all_pokemon(self):
        return self._load_data_from_file()

    def load_pokemon_by_id(self, id):
        # TODO: Have this check cache first before pulling from showdown files
        # -1 because ids start at 1 with Bulbasuar
        return self.load_all_pokemon()[id-1]

    def _process_data(self, jsoned_data):
        # TODO: convert to Pokemon class
        return jsoned_data