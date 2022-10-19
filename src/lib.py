import json

class json_methods:
    def read_json(file_path):
        """
        :param file_path: string
        :return: dict
        """
        file = open(file_path)

        loaded_file = json.load(file)

        return loaded_file
