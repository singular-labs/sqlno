from sqlno.common.dialects import Dialect


class Clause(object):
    def __init__(self, statement):
        self.statement = statement


class EdgeClause(Clause):
    def semicolon(self):
        return str(self.statement) + ';'


class WhereClause(EdgeClause):
    def __init__(self, statement, condition):
        super(WhereClause, self).__init__(statement)
        self.condition = condition

    def __str__(self):
        return 'WHERE {}'.format(str(self.condition))


class FromClause(EdgeClause):
    def __init__(self, statement, *tables):
        super(FromClause, self).__init__(statement)
        self.tables = tables

    def where(self, condition):
        self.statement.where_clause = WhereClause(self.statement, condition)
        return self.statement.where_clause

    def __str__(self):
        return 'FROM {}'.format(', '.join([str(table) for table in self.tables]))


class MySqlOnDuplicateKeyUpdateClause(EdgeClause):
    def __init__(self, statement, *assignments):
        super(MySqlOnDuplicateKeyUpdateClause, self).__init__(statement)
        self.assignments = assignments

    def __str__(self):
        return 'ON DUPLICATE KEY UPDATE {}'.format(
            ', '.join([str(assignment) for assignment in self.assignments])
        )


class ValuesClause(EdgeClause):
    def __init__(self, statement, *values_lists):
        super(ValuesClause, self).__init__(statement)
        self.values_lists = values_lists

    def __str__(self):
        query = 'VALUES {}'.format(
            ', '.join(
                ['({})'.format(','.join([str(value) for value in value_list])) for value_list in self.values_lists]
            )
        )

        return query

    @classmethod
    def create(cls, statement, *values_lists):
        if statement.dialect == Dialect.MYSQL:
            return MySqlValuesClause(statement, *values_lists)
        return ValuesClause(statement, *values_lists)


class MySqlValuesClause(ValuesClause):
    def __init__(self, statement, *values_lists):
        super(MySqlValuesClause, self).__init__(statement, *values_lists)

    def on_duplicate_key_update(self, *assignments):
        self.statement.on_duplicate_key_update_clause = MySqlOnDuplicateKeyUpdateClause(self.statement, *assignments)
        return self.statement.on_duplicate_key_update_clause


class SelectClause(EdgeClause):
    def __init__(self, statement, *columns):
        super(SelectClause, self).__init__(statement)
        self.columns = columns

    def from_(self, *tables):
        self.statement.from_clause = FromClause(self.statement, *tables)
        return self.statement.from_clause

    def __str__(self):
        query = 'SELECT {}'.format(', '.join(self.columns))
        return query

    @classmethod
    def create(cls, statement, *columns):
        return SelectClause(statement, *columns)


class InsertClause(Clause):
    def __init__(self, statement):
        super(InsertClause, self).__init__(statement)

        self.table_name = None
        self.columns = None

    def into(self, table, *columns):
        # type: (str, *str) -> InsertClause
        self.table_name = table
        self.columns = columns
        return self

    def values(self, *values_lists):
        self.statement.values_clause = ValuesClause.create(self.statement, *values_lists)
        return self.statement.values_clause

    def __str__(self):
        clause = 'INSERT'

        if self.table_name is not None:
            clause += ' INTO {}'.format(self.table_name)

        if self.columns is not None:
            clause += ' ({})'.format(','.join(self.columns))

        return clause

    @classmethod
    def create(cls, statement):
        return InsertClause(statement)
