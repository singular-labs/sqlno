from parametrization import Parametrization

from sqlno.common.structures import c, t, db

COLUMN_NAME_0 = 'c_0'

COLUMN_0 = c(COLUMN_NAME_0)

TABLE_NAME_0 = 't_0'
TABLE_ALIAS_0 = 'a_0'

TABLE_0 = t(TABLE_NAME_0)

ALIASED_TABLE_0 = TABLE_0.as_(TABLE_ALIAS_0)

TABLE_COLUMN_0 = TABLE_0.c_0
TABLE_NAMED_COLUMN_0 = TABLE_0.c(COLUMN_NAME_0)
ALIASED_TABLE_COLUMN_0 = ALIASED_TABLE_0.c_0
ALIASED_TABLE_NAMED_COLUMN_0 = ALIASED_TABLE_0.c(COLUMN_NAME_0)

DATABASE_NAME_0 = 'db_0'

DATABASE_0 = db(DATABASE_NAME_0)

DATABASE_TABLE_0 = DATABASE_0.t_0
DATABASE_NAMED_TABLE_0 = DATABASE_0.t(TABLE_NAME_0)
DATABASE_TABLE_COLUMN_0 = DATABASE_TABLE_0.c_0
DATABASE_TABLE_NAMED_COLUMN_0 = DATABASE_TABLE_0.c(COLUMN_NAME_0)

DATABASE_ALIASED_TABLE_0 = DATABASE_TABLE_0.as_(TABLE_ALIAS_0)
DATABASE_ALIASED_NAMED_TABLE_0 = DATABASE_NAMED_TABLE_0.as_(TABLE_ALIAS_0)
DATABASE_ALIASED_TABLE_COLUMN_0 = DATABASE_ALIASED_TABLE_0.c_0
DATABASE_ALIASED_TABLE_NAMED_COLUMN_0 = DATABASE_ALIASED_TABLE_0.c(COLUMN_NAME_0)


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name='c_0',
    expected_query='c_0',
    actual_query=COLUMN_0
)
@Parametrization.case(
    name='t_0',
    expected_query='t_0',
    actual_query=TABLE_0
)
@Parametrization.case(
    name='t_0 as a_0',
    expected_query='t_0 as a_0',
    actual_query=ALIASED_TABLE_0
)
@Parametrization.case(
    name='t_0.c_0',
    expected_query='t_0.c_0',
    actual_query=TABLE_COLUMN_0
)
@Parametrization.case(
    name='t_0.c_0',
    expected_query='t_0.c_0',
    actual_query=TABLE_NAMED_COLUMN_0
)
@Parametrization.case(
    name='a_0.c_0',
    expected_query='a_0.c_0',
    actual_query=ALIASED_TABLE_COLUMN_0
)
@Parametrization.case(
    name='a_0.c_0',
    expected_query='a_0.c_0',
    actual_query=ALIASED_TABLE_NAMED_COLUMN_0
)
@Parametrization.case(
    name='db_0',
    expected_query='db_0',
    actual_query=DATABASE_0
)
@Parametrization.case(
    name='db_0.t_0',
    expected_query='db_0.t_0',
    actual_query=DATABASE_TABLE_0
)
@Parametrization.case(
    name='db_0.t_0',
    expected_query='db_0.t_0',
    actual_query=DATABASE_NAMED_TABLE_0
)
@Parametrization.case(
    name='db_0.t_0.c_0',
    expected_query='db_0.t_0.c_0',
    actual_query=DATABASE_TABLE_COLUMN_0
)
@Parametrization.case(
    name='db_0.t_0.c_0',
    expected_query='db_0.t_0.c_0',
    actual_query=DATABASE_TABLE_NAMED_COLUMN_0
)
@Parametrization.case(
    name='db_0.t_0 as a_0',
    expected_query='db_0.t_0 as a_0',
    actual_query=DATABASE_ALIASED_TABLE_0
)
@Parametrization.case(
    name='db_0.t_0 as a_0',
    expected_query='db_0.t_0 as a_0',
    actual_query=DATABASE_ALIASED_NAMED_TABLE_0
)
@Parametrization.case(
    name='a_0.c_0',
    expected_query='a_0.c_0',
    actual_query=DATABASE_ALIASED_TABLE_COLUMN_0
)
@Parametrization.case(
    name='a_0.c_0',
    expected_query='a_0.c_0',
    actual_query=DATABASE_ALIASED_TABLE_NAMED_COLUMN_0
)
def test_insert(expected_query, actual_query):
    assert str(actual_query) == expected_query
