from parametrization import Parametrization

from sqlno.athena import (
    cast,
)
from sqlno.common.structures import c
from sqlno.mysql import (
    select, astrix, t, set_, insert_into, if_, gte, values, coalesce, case, case_when, e,
)

TEST_TABLE_0 = t('t_0')

TEST_ALIASED_TABLE_0 = TEST_TABLE_0.as_('t_a_0')

TEST_ALIASED_TABLE_0_COLUMN_0 = TEST_ALIASED_TABLE_0.c_0

TEST_COLUMN_0 = c('c_0')
TEST_COLUMN_1 = c('c_1')


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name='minimal',
    expected_query='SELECT *;',
    actual_query=select(astrix).semicolon(),
)
@Parametrization.case(
    name='regular',
    expected_query='SELECT * FROM t_0 as t_a_0 WHERE t_a_0.c_0 > 2;',
    actual_query=select(
        '*'
    ).from_(
        TEST_ALIASED_TABLE_0
    ).where(
        TEST_ALIASED_TABLE_0_COLUMN_0 > 2
    ).semicolon(),
)
def test_select(expected_query, actual_query):
    assert str(actual_query) == expected_query


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name='minimal',
    expected_query='INSERT INTO t_0 (c_0) VALUES (1) ON DUPLICATE KEY UPDATE c_1 = 4;',
    actual_query=insert_into(
        TEST_TABLE_0, TEST_COLUMN_0
    ).values([1]).on_duplicate_key_update(
        set_(TEST_COLUMN_1, 4)
    ).semicolon(),
)
@Parametrization.case(
    name='without_structures',
    expected_query='INSERT INTO t_0 (c_0) VALUES (1) ON DUPLICATE KEY UPDATE c_1 = 4;',
    actual_query=insert_into(
        't_0', 'c_0'
    ).values([1]).on_duplicate_key_update(
        set_('c_1', 4)
    ).semicolon(),
)
@Parametrization.case(
    name='without_structures_and_string_set',
    expected_query='INSERT INTO t_0 (c_0) VALUES (1) ON DUPLICATE KEY UPDATE c_1 = 4;',
    actual_query=insert_into(
        't_0', 'c_0'
    ).values([1]).on_duplicate_key_update(
        'c_1 = 4'
    ).semicolon(),
)
@Parametrization.case(
    name='without_structures_and_string_set',
    expected_query='INSERT INTO t_0 (c_0) VALUES (1) '
                   'ON DUPLICATE KEY UPDATE '
                   'c_1 = if(values(c_0) >= coalesce(c_0, -1), values(c_0), c_0)'
                   ';',
    actual_query=insert_into(
        TEST_TABLE_0, TEST_COLUMN_0
    ).values([1]).on_duplicate_key_update(
        set_(
            TEST_COLUMN_1,
            if_(gte(values(TEST_COLUMN_0), coalesce(TEST_COLUMN_0, -1)), values(TEST_COLUMN_0), TEST_COLUMN_0)
        )
    ).semicolon()
)
@Parametrization.case(
    name='without_structures_and_string_set',
    expected_query='INSERT INTO t_0 (c_0, c_1) VALUES (1,2),(2,3);',
    actual_query=insert_into(
        TEST_TABLE_0, TEST_COLUMN_0, TEST_COLUMN_1
    ).values([1, 2], [2, 3]).semicolon()
)
def test_insert(expected_query, actual_query):
    assert str(actual_query) == expected_query


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
