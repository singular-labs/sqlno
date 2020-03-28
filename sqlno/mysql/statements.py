from sqlno.common.clauses import InsertClause
from sqlno.common.statements import InsertContext
from sqlno.mysql.clauses import MySqlValuesClause


class MySqlInsertContext(InsertContext):
    VALUES_CLAUSE = MySqlValuesClause

    def __init__(self):
        super(InsertContext, self).__init__()
        self.on_duplicate_key_update_clause = None

    @property
    def clauses(self):
        return filter(None, super(MySqlInsertContext, self).clauses + [self.on_duplicate_key_update_clause])


def insert_into(table, *columns):
    return InsertClause(MySqlInsertContext()).into(table, *columns)
