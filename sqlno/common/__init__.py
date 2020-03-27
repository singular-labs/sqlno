from sqlno.common.statements import SelectStatement


def select(*columns):
    return SelectStatement.create(engine).select(*columns)


def insert_into(table_name, *columns):
    return InsertStatement.create(engine).insert().into(table_name, *columns)
