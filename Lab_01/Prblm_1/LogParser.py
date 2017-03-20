import argparse


class LogParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_log(input_file, string_to_be_found):
        result = []
        with open(input_file, "r") as file_object:
            data = file_object.read()
            file_object.close()
        split_data = data.split("\n")
        for string in split_data:
            if string_to_be_found in string:
                result.append(string)
        return result

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(description = "File path: ")
        parser.add_argument("file_object", type = str)
        arg = parser.parse_args()
        return arg.file_object

    @staticmethod
    def save_result(file_to_save, result):
        with open(file_to_save, "w") as result_file:
            for line in result:
                result_file.write(line)
                result_file.write("\n")
            result_file.close()



