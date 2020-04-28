from collections import namedtuple

from six import iteritems

from sqlno.common import *
from sqlno.common.aliases import *
from sqlno.common.clauses import Clause, EdgeClause
from sqlno.common.functions import *
from sqlno.common.expressions import *
from sqlno.athena.functions import *
from sqlno.common.statements import StatementContext


class ShowContext(StatementContext):
    @property
    def clauses(self):
        return [self.show_clause]

    def __init__(self):
        self.show_clause = None


class ShowPartitionClause(EdgeClause):
    def __init__(self, context, table):
        super(ShowPartitionClause, self).__init__(context)
        self.context.show_clause = self
        self.table = table

    def __str__(self):
        return 'SHOW PARTITIONS {}'.format(str(self.table))


def show_partitions(table):
    return ShowPartitionClause(ShowContext(), table)


class AlterContext(StatementContext):
    @property
    def clauses(self):
        return [self.alter_clause, self.action_clause]

    def __init__(self):
        self.alter_clause = None
        self.action_clause = None


class AlterClause(Clause):
    def __init__(self, context):
        super(AlterClause, self).__init__(context)

    def table(self, table_name):
        return AlterTableClause(self.context, table_name)


class AlterTableClause(Clause):
    def __init__(self, context, table_name):
        super(AlterTableClause, self).__init__(context)
        self.context.alter_clause = self
        self.table_name = table_name

    def drop(self, *partitions):
        return DropClause(self.context, partitions)

    def drop_if_exists(self, *partitions):
        return DropClause(self.context, partitions, if_exists=True)

    def __str__(self):
        return 'ALTER TABLE {}'.format(self.table_name)


class DropClause(EdgeClause):
    def __init__(self, context, partitions, if_exists=False):
        super(DropClause, self).__init__(context)
        self.context.action_clause = self
        self.partitions = partitions
        self.if_exists = if_exists

    def __str__(self):
        clause = 'DROP '

        if self.if_exists:
            clause += 'IF EXISTS '

        clause += ', '.join(map(str, self.partitions))

        return clause


class Partition(object):
    def __init__(self, *columns):
        self.columns = columns

    def __str__(self):
        return 'PARTITION ({})'.format(
            ', '.join(map(str, self.columns))
        )


partition = Partition


def alter_table(table):
    return AlterClause(AlterContext()).table(table)
