# noinspection PyUnresolvedReferences
from sqlno.common.aliases import (astrix, set_, gte, case, case_when, p, is_not, null, ne, or_, and_, is_)
# noinspection PyUnresolvedReferences
from sqlno.common.functions import if_, values, coalesce, current_timestamp
from sqlno.common.statements import SelectStatement, InsertStatement
# noinspection PyUnresolvedReferences
from sqlno.common.structures import Table
from sqlno.mysql import engine


def select(*columns):
    return SelectStatement.create(engine).select(*columns)


def insert_into(table_name, *columns):
    return InsertStatement.create(engine).insert().into(table_name, *columns)


t = Table
