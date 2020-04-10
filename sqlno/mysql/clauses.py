from sqlno.common.clauses import ValuesClause, EdgeClause


class MySqlValuesClause(ValuesClause):
    def __init__(self, context, *values_lists):
        super(MySqlValuesClause, self).__init__(context, *values_lists)

    def on_duplicate_key_update(self, *assignments):
        return OnDuplicateKeyUpdateClause(self.context, *assignments)


class OnDuplicateKeyUpdateClause(EdgeClause):
    def __init__(self, statement, *assignments):
        super(OnDuplicateKeyUpdateClause, self).__init__(statement)
        self.context.on_duplicate_key_update_clause = self
        self.assignments = assignments

    def __str__(self):
        return 'ON DUPLICATE KEY UPDATE {}'.format(
            ','.join([str(assignment) for assignment in self.assignments])
        )
