import unittest
from src.sqlite import *

class TestSqlite(unittest.TestCase):

    def setUp(self):
        self.table_1 = 'lol'
        self.columns_1 = {'id': 'INTEGER PRIMARY KEY',
                          'name': 'VARCHAR(20) NOT NULL',
                          'timestamp': 'DATETIME NOT NULL'}
        self.table_2 = 'p_key_composite'
        self.columns_2 = {'id': 'INTEGER NOT NULL',
                          'name': 'VARCHAR(20) NOT NULL',
                          'timestamp': 'DATETIME NOT NULL',
                          'PRIMARY KEY': '(id, name)'}

    def test_CreateSqlite(self):
        create_query = CreateSqlite(self.table_1, self.columns_1)
        expected = f'CREATE TABLE IF NOT EXISTS {self.table_1} (id INTEGER PRIMARY KEY, name VARCHAR(20) NOT NULL, timestamp DATETIME NOT NULL);'
        actual = create_query.generate()
        self.assertEqual(expected, actual)

    def test_CreateSqliteWithCompositePrimaryKey(self):
        create_query = CreateSqlite(self.table_2, self.columns_2)
        expected = f'CREATE TABLE IF NOT EXISTS {self.table_2} (id INTEGER NOT NULL, name VARCHAR(20) NOT NULL, timestamp DATETIME NOT NULL, PRIMARY KEY (id, name));'
        actual = create_query.generate()
        self.assertEqual(expected, actual)

    def test_InsertSqlite(self):
        insert_query = InsertSqlite(self.table_1, self.columns_1)
        expected = f'INSERT INTO {self.table_1} VALUES (?, ?, ?)'
        actual = insert_query.generate()
        self.assertEqual(expected, actual)

    def test_InsertSqliteWithCompositePrimaryKey(self):
        insert_query = InsertSqlite(self.table_2, self.columns_2)
        expected = f'INSERT INTO {self.table_2} VALUES (?, ?, ?)'
        actual = insert_query.generate()
        self.assertEqual(expected, actual)

    def test_SelectSqlite(self):
        select_all_query = SelectSqlite(self.table_1, self.columns_1)
        expected = f'SELECT * FROM {self.table_1};'
        actual = select_all_query.generate()
        self.assertEqual(expected, actual)
