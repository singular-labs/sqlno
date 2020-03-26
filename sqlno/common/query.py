from sqlno.common.statements import SelectStatement, InsertStatement


class Query(object):
    def __init__(self, dialect):
        self.dialect = dialect

    def select(self, *columns):
        return SelectStatement.create(self.dialect).select(*columns)

    def insert_into(self, table_name, *columns):
        return InsertStatement.create(self.dialect).insert().into(table_name, *columns)
