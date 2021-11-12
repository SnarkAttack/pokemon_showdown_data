from loaders.base_loader import FunctionRemovalLoader

class ConditionLoader(FunctionRemovalLoader):

    def __init__(self):
        super().__init__('conditions.ts')

    def load_all_conditions(self):
        return self._load_data_from_file()

    def load_condition_by_key(self, key):
        return self._load_data_from_file()[key]

    def _process_data(self, condition_data):
        return condition_data

    def _save_to_database(self, condition_data):
        pass
    