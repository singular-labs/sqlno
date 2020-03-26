from sqlno.common.statements import InsertStatement as CommonInsertStatement


class InsertStatement(CommonInsertStatement):
    def __init__(self, dialect):
        super(InsertStatement, self).__init__(dialect)
        self.on_duplicate_key_update_clause = None

    @property
    def clauses(self):
        return filter(None, super(InsertStatement, self).clauses + [self.on_duplicate_key_update_clause])
