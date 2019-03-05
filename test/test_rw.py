import unittest
from pathlib import Path
from src.rw import RESOURCE_FOLDER, save_file, read_file


class TestReadWrite(unittest.TestCase):

    def setUp(self):
        JSON_EXT = ".json"
        self.file_one = "one"
        self.file_two = "two"
        self.path_file_one = RESOURCE_FOLDER / (self.file_one + JSON_EXT)
        self.path_file_two = RESOURCE_FOLDER / (self.file_two + JSON_EXT)
        self.data_one = '{"apex": "legends"}'
        self.data_two = '{"garbage": "can"}'

    def test_save_file(self):
        save_file(self.file_one)
        save_file(self.file_two)
        self.assertTrue(self.path_file_one.exists())
        self.assertTrue(self.path_file_two.exists())

    def test_read_file(self):
        save_file(self.file_one, data=self.data_one)
        data = read_file(self.file_one)
        self.assertEqual(data, {"apex": "legends"})

    def test_read_file_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: read_file('three'))

    def tearDown(self):
        if self.path_file_one.exists():
            self.path_file_one.unlink()
        if self.path_file_two.exists():
            self.path_file_two.unlink()
