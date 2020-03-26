from sqlno.expressions import GreaterThenOperator


class IntegerColumn(object):
    def __init__(self, table, name):
        self.table = table
        self.name = name

    def greater_then(self, value):
        return GreaterThenOperator(self, value)

    def __str__(self):
        return str(self.table.name) + '.' + self.name


class AliasedTable(object):
    def __init__(self, name, alias):
        self._name = name
        self.alias = alias

    def integer_column(self, name):
        return IntegerColumn(self, name)

    @property
    def name(self):
        return self.alias

    def __str__(self):
        return '{} as {}'.format(self._name, self.alias)


class Table(object):
    def __init__(self, name):
        self.name = name

    def as_(self, alias):
        return AliasedTable(self.name, alias)
