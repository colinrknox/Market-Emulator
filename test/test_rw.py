import unittest
import os
from src.rw import RESOURCE_PATH, save_file, read_file


class TestReadWrite(unittest.TestCase):

    def setUp(self):
        self.file_one = 'one'
        self.file_two = 'two'
        self.data_one = '{"colin": "knox"}'
        self.data_two = '{"seth": "knox"}'

    def test_save_file(self):
        save_file(self.file_one)
        save_file(self.file_two)
        self.assertTrue(os.path.isfile(RESOURCE_PATH + self.file_one + '.json'))
        self.assertTrue(os.path.isfile(RESOURCE_PATH + self.file_two + '.json'))

    def test_read_file(self):
        save_file(self.file_one, data=self.data_one)
        data = read_file(self.file_one)
        self.assertEqual(data, {'colin': 'knox'})

    def test_read_file_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: read_file('three'))

    def tearDown(self):
        if os.path.isfile(RESOURCE_PATH + self.file_one + '.json'):
            os.remove(RESOURCE_PATH + self.file_one + '.json')
        if os.path.isfile(RESOURCE_PATH + self.file_two + '.json'):
            os.remove(RESOURCE_PATH + self.file_two + '.json')
