from abc import ABCMeta, abstractmethod


class SqliteQuery(metaclass=ABCMeta):
    """Abstract base class for any class that generates a Sqlite query"""
    @abstractmethod
    def __init__(self, table, columns):
        self.table = table
        self.columns = columns

    @abstractmethod
    def generate(self):
        raise NotImplementedError(f'{self.__class__.__name__} needs to implement Sqlite.generate()')


class CreateSqlite(SqliteQuery):
    def __init__(self, table, columns):
        super().__init__(table, columns)

    def generate(self):
        result = f'CREATE TABLE IF NOT EXISTS {self.table} ('
        result = result + ', '.join([f'{k} {v}' for k, v in self.columns.items()])
        result = result + ');'
        return result


class InsertSqlite(SqliteQuery):
    def __init__(self, table, columns):
        super().__init__(table, columns)

    def generate(self):
        return f'INSERT INTO {self.table} VALUES ({", ".join(["?" for k,v in self.columns.items() if k != "PRIMARY KEY"])})'


class SelectSqlite(SqliteQuery):
    def __init__(self, table, columns):
        super().__init__(table, columns)

    def generate(self):
        return f'SELECT * FROM {self.table};'
