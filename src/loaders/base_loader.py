import os
import re
import abc
import json

from utils import get_package_root

def remove_comments(ts_pair_str):
    """
    Find any instances of '//' and remove them and everything that follows
    """
    comment_location = ts_pair_str.find('//')

    if comment_location == -1:
        return ts_pair_str
    else:
        return ts_pair_str[:comment_location]

def quote_enclose_key(ts_pair_str):

    # Colon must be part of the group, otherwise the replace() call can add unexpected quotations
    # (seen in hidden abilities that start with H, which is also the hidden ability key)
    pattern = re.compile(r'([\w]+:)')

    matches = pattern.findall(ts_pair_str)

    for match in matches:
        # This is a specific case to catch Type: Null's name
        # TODO: Move this check somewhere else, too specific of a case to just in a utility method
        # Maybe make quote_enclose_key a class method so each loader can override as needed
        if match != "Type:":
            ts_pair_str = ts_pair_str.replace(match, f'\"{match[:-1]}\":')

    return ts_pair_str

def remove_trailing_commas(json_str):
    """
    Removes trailing commas that will break the json.loads() call
    """
    json_str = re.sub(r',[ ]*}', r'}', json_str)
    json_str = re.sub(r',[ ]*]', r']', json_str)

    return json_str

def ts_to_json(ts_str_list):

    uncommented_strs = [remove_comments(ts_str) for ts_str in ts_str_list]
    quoted_strs = [quote_enclose_key(ts_str) for ts_str in uncommented_strs]
    return ''.join(quoted_strs)

class BaseLoader(abc.ABC):

    def __init__(self, filename):
        self.filename = os.path.join(get_package_root(), 'pokemon-showdown', 'data', filename)

    def _load_data_from_file(self):
        """
        Load the entirety of a file into classes defiend by subclass' process_data() function
        """

        full_file_data = []

        try:
            with open(self.filename, 'r') as f:
                lines = [l.strip() for l in f.readlines()]

            ts_data_chunk = []

            for l in lines:
                # Start of pokemon's data
                if re.match(r'^[a-z0-9]+: {$', l):
                    ts_data_chunk.append(l)
                # Terminate collection for a pokemon
                elif l == '},':
                    ts_data_chunk.append(l)

                    # At this point pokemon_data holds everything for a given pokemon, so
                    # convert it from the typescript format into json
                    jsoned_chunk = ts_to_json(ts_data_chunk)

                    processed_data = self._process_data(jsoned_chunk)

                    full_file_data.append(processed_data)
                    ts_data_chunk = []
                # Means we are in the middle of a pokemon's data
                elif len(ts_data_chunk) != 0:
                    ts_data_chunk.append(l)

            dicted_str = f"{{{''.join(full_file_data)}}}"
            cleaned_str = remove_trailing_commas(dicted_str)

            file_dict = json.loads(cleaned_str)

            print(file_dict)

            return file_dict
        except IOError as e:
            raise e

    @abc.abstractmethod
    def _process_data(self, data):
        raise NotImplementedError()