from sqlno.common.clauses import ValuesClause as CommonValuesClause, EdgeClause


class ValuesClause(CommonValuesClause):
    def __init__(self, statement, *values_lists):
        super(ValuesClause, self).__init__(statement, *values_lists)

    def on_duplicate_key_update(self, *assignments):
        self.statement.on_duplicate_key_update_clause = OnDuplicateKeyUpdateClause(self.statement, *assignments)
        return self.statement.on_duplicate_key_update_clause


class OnDuplicateKeyUpdateClause(EdgeClause):
    def __init__(self, statement, *assignments):
        super(OnDuplicateKeyUpdateClause, self).__init__(statement)
        self.assignments = assignments

    def __str__(self):
        return 'ON DUPLICATE KEY UPDATE {}'.format(
            ', '.join([str(assignment) for assignment in self.assignments])
        )
