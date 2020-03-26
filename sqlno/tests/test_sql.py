from sqlno import CASE_WHEN
from sqlno.aliases import ASTRIX, GTE, SET, CASE
from sqlno.expressions import Assignment
from sqlno.functions import Values, If, Coalesce
from sqlno.query import mysql
from sqlno.structures import Table


def test_select():
    assert 'SELECT *;' == mysql.select(ASTRIX).semicolon()

    table_alias = Table('table_name').as_('table_alias')
    condition = table_alias.integer_column('column_name').greater_then(2)

    assert 'SELECT * FROM table_name as table_alias WHERE table_alias.column_name > 2;' == mysql.select(
        ASTRIX
    ).from_(
        table_alias
    ).where(
        condition
    ).semicolon()

    assert 'SELECT * FROM table_name as table_alias WHERE table_alias.column_name > 2;' == mysql.select(
        '*'
    ).from_(
        'table_name as table_alias'
    ).where(
        'table_alias.column_name > 2'
    ).semicolon()


def test_insert():
    expected_query = 'INSERT INTO table_name (column_name) VALUES (1) ON DUPLICATE KEY UPDATE column_name_2 = 4;'

    assert expected_query == mysql.insert_into(
        'table_name', 'column_name'
    ).values([1]).on_duplicate_key_update(
        Assignment('column_name_2', 4)
    ).semicolon()

    expected_query = 'INSERT INTO table_name (column_name) VALUES (1) ON DUPLICATE KEY UPDATE column_name_2 = 4;'

    assert expected_query == mysql.insert_into(
        'table_name', 'column_name'
    ).values([1]).on_duplicate_key_update(
        'column_name_2 = 4'
    ).semicolon()

    expected_query = 'INSERT INTO t (c1) VALUES (1) ' \
                     'ON DUPLICATE KEY UPDATE ' \
                     'c2 = IF(VALUES(c1) >= COALESCE(c1, -1), VALUES(c1), c1)' \
                     ';'

    assert expected_query == mysql.insert_into(
        't', 'c1'
    ).values([1]).on_duplicate_key_update(
        SET('c2', If(GTE(Values('c1'), Coalesce('c1', -1)), Values('c1'), 'c1'))
    ).semicolon()


def test_insert_with_multiple_values():
    expected_query = 'INSERT INTO t (c1,c2) VALUES (1,2), (2,3);'

    assert expected_query == mysql.insert_into(
        't', 'c1', 'c2'
    ).values([1, 2], [2, 3]).semicolon()


def test_case():
    expected_query = "SELECT CASE 1 WHEN 1 THEN 'one' WHEN 2 THEN 'two' ELSE 'more' END;"

    assert mysql.select(
        CASE(1).when(1).then("'one'").when(2).then("'two'").else_("'more'").end()
    ).semicolon() == expected_query

    expected_query = "SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;"

    assert mysql.select(
        CASE_WHEN('1>0').then("'true'").else_("'false'").end()
    ).semicolon() == expected_query
