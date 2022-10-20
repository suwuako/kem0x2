import json
import datetime

class json_methods:
    def read_json(file_path):
        """
        :param file_path: string
        :return: dict
        """
        file = open(file_path)

        loaded_file = json.load(file)

        return loaded_file

class logging:
    def get_timestamp():
        current_time = datetime.datetime.now()
        formatted_time = f"[`{current_time.hour}:{current_time.minute}:{current_time.second}` `({current_time.day}/{current_time.month})`]"

        return formatted_time

