from sqlno.common.clauses import SelectClause, InsertClause, ValuesClause


class StatementContext(object):
    @property
    def clauses(self):
        raise NotImplementedError()

    def __str__(self):
        return ' '.join(map(str, self.clauses))


class SelectContext(StatementContext):
    def __init__(self):
        self.select_clause = None
        self.from_clause = None
        self.where_clause = None

    @property
    def clauses(self):
        return filter(None, [self.select_clause, self.from_clause, self.where_clause])


def select(*columns):
    return SelectClause(SelectContext(), *columns)


class InsertContext(StatementContext):
    VALUES_CLAUSE = ValuesClause

    def __init__(self):
        self.insert_clause = None
        self.values_clause = None

    @property
    def clauses(self):
        return [self.insert_clause, self.values_clause]


def insert_into(table, columns):
    return InsertClause(InsertContext()).into(table, columns)
