from sqlno.common.clauses import SelectClause, InsertClause


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
    def __init__(self, engine):
        super(InsertStatement, self).__init__(engine)

        self.insert_clause = None
        self.values_clause = None

    def insert(self):
        self.insert_clause = InsertClause.create(self)
        return self.insert_clause

    @property
    def clauses(self):
        return [self.insert_clause, self.values_clause]

    @classmethod
    def create(cls, engine):
        return engine.insert_statement_cls(engine)
