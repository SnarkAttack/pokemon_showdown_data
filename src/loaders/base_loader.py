import os
import re
import abc
import json
from collections import Counter

from utils import get_package_root

class BaseLoader(abc.ABC):

    def __init__(self, filename):
        self.filename = os.path.join(get_package_root(), 'pokemon-showdown', 'data', filename)

        self.filter = False

    def _remove_comments(self, ts_pair_str):
        """
        Find any instances of '//' and remove them and everything that follows
        """
        comment_location = ts_pair_str.find('//')

        if comment_location == -1:
            return ts_pair_str
        else:
            return ts_pair_str[:comment_location]

    def _quote_enclose_key(self, ts_pair_str):

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

    def _remove_trailing_commas(self, json_str):
        """
        Removes trailing commas that will break the json.loads() call
        """
        json_str = re.sub(r',[ ]*}', r'}', json_str)
        json_str = re.sub(r',[ ]*]', r']', json_str)

        return json_str

    def _ts_to_json(self, ts_str_list):

        uncommented_strs = [self._remove_comments(ts_str) for ts_str in ts_str_list]
        quoted_strs = [self._quote_enclose_key(ts_str) for ts_str in uncommented_strs]
        return ''.join(quoted_strs)

    def _filter_line(self, l):
        """
        Return True if the line should be ignored
        """
        return False

    def _load_data_from_file(self):
        """
        Load the entirety of a file into classes defiend by subclass' process_data() function
        """

        full_file_data = []

        with open(self.filename, 'r') as f:
            lines = [l.strip() for l in f.readlines()]

        ts_data_chunk = []
        capturing_data = False
        filtering = False
        braces = 0
        braces_at_filter = 0

        for l in lines:
            # Start of pokemon's data
            if re.match(r'^[a-z0-9]+: {$', l):
                capturing_data = True


            if capturing_data:

                # Check if this line should start the filtering process OR we are already filtering
                if not self._filter_line(l) and not filtering:
                    ts_data_chunk.append(l)
                else:
                    if not filtering:
                        braces_at_filter = braces
                    filtering = True

                braces += l.count('{')
                braces -= l.count('}')

                if braces < 0:
                    raise ValueError("File formatted incorrectly, braces do not match")

                if braces <= braces_at_filter:
                    filtering = False

                if braces == 0:
                    # At this point ts_data_chunk holds everything for a given pokemon, so
                    # convert it from the typescript format into json
                    jsoned_chunk = self._ts_to_json(ts_data_chunk)

                    processed_data = self._process_data(jsoned_chunk)

                    full_file_data.append(processed_data)
                    ts_data_chunk = []
                    capturing_data = False

        dicted_str = f"{{{''.join(full_file_data)}}}"
        cleaned_str = self._remove_trailing_commas(dicted_str)

        file_dict = json.loads(cleaned_str)

        return file_dict

    def get_field_frequency(self):
        data = self._load_data_from_file()
        fields = []
        for v in data.values():
            fields += v.keys()
        c = Counter(fields)
        return c

    @abc.abstractmethod
    def _process_data(self, data):
        raise NotImplementedError()

    @abc.abstractmethod
    def _save_to_database(self, cls_object):
        raise not NotImplementedError()

class FunctionRemovalLoader(BaseLoader, abc.ABC):

    def __init__(self, filename):
        super().__init__(filename)

    def _filter_line(self, l):
        if '(' in l and ')' in l:
            return True
        return False
