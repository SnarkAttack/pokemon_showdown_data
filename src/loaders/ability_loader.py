from .base_loader import FunctionRemovalLoader

class AbilityLoader(FunctionRemovalLoader):

    def __init__(self):
        super().__init__('abilities.ts')

    def load_all_abilities(self):
        return self._load_data_from_file()

    def load_ability_by_name(self, name):
        return self.load_all_abilities()[name]

    def _process_data(self, ability_data):
        return ability_data

    def _save_to_database(self, ability_obj):
        pass
    