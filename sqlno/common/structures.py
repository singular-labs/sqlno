from sqlno.common.expressions import Expression


class TableColumn(Expression):
    def __init__(self, name, table_name=None, database_name=None):
        super(TableColumn, self).__init__('.'.join(filter(None, [database_name, table_name, name])))


class Table(object):
    def __init__(self, name, database_name=None):
        self.name = name
        self.database_name = database_name

        self.columns = {}

    def c(self, column_name):
        column = TableColumn(column_name, table_name=self.name, database_name=self.database_name)
        self.columns[column_name] = column
        return column

    def __getattr__(self, attribute_name):
        return self.c(attribute_name)

    def as_(self, alias):
        return AliasedTable(self.name, alias, database_name=self.database_name)

    def __str__(self):
        return '.'.join(filter(None, [self.database_name, self.name]))


class AliasedTable(Table):
    def __init__(self, name, alias, database_name=None):
        super(AliasedTable, self).__init__(name, database_name=database_name)
        self.alias = alias

    def c(self, column_name):
        column = TableColumn(column_name, table_name=self.alias)
        self.columns[column_name] = column
        return column

    def __str__(self):
        return '{} as {}'.format(super(AliasedTable, self).__str__(), self.alias)


class Database(object):
    def __init__(self, name):
        super(Database, self).__init__()
        self.name = name

        self.tables = {}

    def t(self, table_name):
        table = Table(table_name, database_name=self.name)
        self.tables[table_name] = table
        return table

    def __getattr__(self, table_name):
        return self.t(table_name)

    def __str__(self):
        return self.name


_global_database = Database(None)

_global_table = Table(None)


def db(database_name):
    return Database(database_name)


def t(table_name):
    return getattr(_global_database, table_name)


def c(column_name):
    return getattr(_global_table, column_name)
