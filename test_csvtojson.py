import unittest
import csvtojson
import os

# Creating a Class for defining Test Cases

class TestCsvJson(unittest.TestCase):

    def test_read_csv(self):
        # To test the functionality of csv file reading / Exception Handling
        file = csvtojson.read_csv()
        input_file_path, input_file_extension = os.path.splitext(file)
        self.assertEqual(input_file_extension, '.csv')

    def test_load_parentDict(self):
        # To test the functionality of loading parentDict from DataFrame
        level1name, level1id = csvtojson.load_parentDict()
        self.assertEqual(level1name, 'THE BEST')
        self.assertEqual(level1id, '178974')

    def test_load_childDict(self):
        # To test the functionality of loading childDict from DataFrame
        level2name, level2id = csvtojson.load_childDict()
        self.assertEqual(level2name, 'DRINKS')
        self.assertEqual(level2id, '178973')

    def test_load_json(self):
        # To check with the json file / Exception Handling
        json_file = csvtojson.load_json()
        output_file_path, output_file_extension = os.path.splitext(json_file)
        self.assertEqual(output_file_extension, '.json')


if __name__ == '__main__':
    unittest.main()






