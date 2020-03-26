from sqlno.common.clauses import SelectClause, InsertClause
from sqlno.common.dialects import Dialect


class Statement(object):
    def __init__(self, dialect):
        self.dialect = dialect

    @property
    def clauses(self):
        raise NotImplementedError()

    def __str__(self):
        return ' '.join(map(str, self.clauses))


class SelectStatement(Statement):
    def __init__(self, dialect):
        super(SelectStatement, self).__init__(dialect)

        self.select_clause = None
        self.from_clause = None
        self.where_clause = None

    def select(self, *columns):
        self.select_clause = SelectClause(self, *columns)
        return self.select_clause

    @property
    def clauses(self):
        return filter(None, [self.select_clause, self.from_clause, self.where_clause])

    @classmethod
    def create(cls, dialect):
        return SelectStatement(dialect)


class InsertStatement(Statement):
    def __init__(self, dialect):
        super(InsertStatement, self).__init__(dialect)

        self.insert_clause = None
        self.values_clause = None

    def insert(self):
        self.insert_clause = InsertClause.create(self)
        return self.insert_clause

    @property
    def clauses(self):
        return [self.insert_clause, self.values_clause]

    @classmethod
    def create(cls, dialect):
        if dialect == Dialect.MYSQL:
            return MySqlInsertStatement(dialect)
        return InsertStatement(dialect)


class MySqlInsertStatement(InsertStatement):
    def __init__(self, dialect):
        super(MySqlInsertStatement, self).__init__(dialect)
        self.on_duplicate_key_update_clause = None

    @property
    def clauses(self):
        return filter(None, super(MySqlInsertStatement, self).clauses + [self.on_duplicate_key_update_clause])
