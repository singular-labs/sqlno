class Clause(object):
    def __init__(self, context):
        self.context = context


class EdgeClause(Clause):
    def semicolon(self):
        return str(self.context) + ';'


class WhereClause(EdgeClause):
    def __init__(self, context, condition):
        super(WhereClause, self).__init__(context)
        self.context.where_clause = self
        self.condition = condition

    def __str__(self):
        return 'WHERE {}'.format(str(self.condition))


class FromClause(EdgeClause):
    def __init__(self, context, *tables):
        super(FromClause, self).__init__(context)
        self.context.from_clause = self
        self.tables = tables

    def where(self, condition):
        return WhereClause(self.context, condition)

    def __str__(self):
        return 'FROM {}'.format(', '.join([str(table) for table in self.tables]))


class ValuesClause(EdgeClause):
    def __init__(self, context, *values_lists):
        super(ValuesClause, self).__init__(context)
        self.context.values_clause = self
        self.values_lists = values_lists

    def __str__(self):
        query = 'VALUES {}'.format(
            ','.join(
                ['({})'.format(','.join([str(value) for value in value_list])) for value_list in self.values_lists]
            )
        )

        return query


class SelectClause(EdgeClause):
    def __init__(self, context, *columns):
        super(SelectClause, self).__init__(context)
        self.context.select_clause = self
        self.columns = columns

    def from_(self, *tables):
        return FromClause(self.context, *tables)

    def __str__(self):
        query = 'SELECT {}'.format(', '.join(self.columns))
        return query


class InsertClause(Clause):
    def __init__(self, context):
        super(InsertClause, self).__init__(context)
        self.context.insert_clause = self

        self.table_name = None
        self.columns = None

    def into(self, table, *columns):
        # type: (str, *str) -> InsertClause
        self.table_name = table
        self.columns = columns
        return self

    def values(self, *values_lists):
        return self.context.VALUES_CLAUSE(self.context, *values_lists)

    def __str__(self):
        clause = 'INSERT'

        if self.table_name is not None:
            clause += ' INTO {}'.format(self.table_name)

        if self.columns is not None:
            clause += ' ({})'.format(', '.join(map(str, self.columns)))

        return clause
