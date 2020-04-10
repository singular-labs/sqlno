from sqlno.common.expressions import e, Expression


class TableColumn(Expression):
    def __init__(self, name):
        super(TableColumn, self).__init__(name)
        

class AnonymousTable(object):
    def __getattr__(self, column_name):
        column = TableColumn(column_name)
        setattr(self, column_name, TableColumn(column_name))
        return column

    def __str__(self):
        raise NotImplementedError()


class AliasedTable(AnonymousTable):
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

    def __getattr__(self, column_name):
        return super(AliasedTable, self).__getattr__('{}.{}'.format(self.alias, column_name))

    def __str__(self):
        return '{} as {}'.format(self.name, self.alias)


class Table(AnonymousTable):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, column_name):
        return super(Table, self).__getattr__('{}.{}'.format(self.name, column_name))

    def as_(self, alias):
        return AliasedTable(self.name, alias)

    def __str__(self):
        return self.name


_global_table = AnonymousTable()

t = Table


def c(column_name):
    return getattr(_global_table, column_name)
