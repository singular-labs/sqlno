from sqlno import p, and_, s
from sqlno.mysql import (
    select, astrix, t, set_, insert_into, if_, gte, values, coalesce, case, case_when, e
)
from sqlno.athena import (
    cast,
    greatest,
    floor,
    to_unixtime,
    lower,
    json_extract_scalar,
)


def test_select():
    assert 'SELECT *;' == select(astrix).semicolon()

    table_alias = t('table_name').as_('table_alias')
    condition = table_alias.integer_column('column_name').greater_then(2)

    assert 'SELECT * FROM table_name as table_alias WHERE table_alias.column_name > 2;' == select(
        astrix
    ).from_(
        table_alias
    ).where(
        condition
    ).semicolon()

    assert 'SELECT * FROM table_name as table_alias WHERE table_alias.column_name > 2;' == select(
        '*'
    ).from_(
        'table_name as table_alias'
    ).where(
        'table_alias.column_name > 2'
    ).semicolon()


def test_insert():
    expected_query = 'INSERT INTO table_name (column_name) VALUES (1) ON DUPLICATE KEY UPDATE column_name_2 = 4;'

    assert insert_into(
        'table_name', 'column_name'
    ).values([1]).on_duplicate_key_update(
        set_('column_name_2', 4)
    ).semicolon() == expected_query

    expected_query = 'INSERT INTO table_name (column_name) VALUES (1) ON DUPLICATE KEY UPDATE column_name_2 = 4;'

    assert expected_query == insert_into(
        'table_name', 'column_name'
    ).values([1]).on_duplicate_key_update(
        'column_name_2 = 4'
    ).semicolon()

    expected_query = 'INSERT INTO t (c1) VALUES (1) ' \
                     'ON DUPLICATE KEY UPDATE ' \
                     'c2 = if(values(c1) >= coalesce(c1, -1), values(c1), c1)' \
                     ';'

    assert expected_query == insert_into(
        't', 'c1'
    ).values([1]).on_duplicate_key_update(
        set_('c2', if_(gte(values('c1'), coalesce('c1', -1)), values('c1'), 'c1'))
    ).semicolon()


def test_insert_with_multiple_values():
    expected_query = 'INSERT INTO t (c1,c2) VALUES (1,2), (2,3);'

    assert expected_query == insert_into(
        't', 'c1', 'c2'
    ).values([1, 2], [2, 3]).semicolon()


def test_case():
    expected_query = "SELECT CASE 1 WHEN 1 THEN 'one' WHEN 2 THEN 'two' ELSE 'more' END;"

    assert select(
        case(1).when(1).then("'one'").when(2).then("'two'").else_("'more'").end()
    ).semicolon() == expected_query

    expected_query = "SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;"

    assert select(
        case_when('1>0').then("'true'").else_("'false'").end()
    ).semicolon() == expected_query


def test_cast():
    expected_expression = "cast(bla AS BIGINT)"

    assert str(cast('bla', 'BIGINT')) == expected_expression
