from parametrization import Parametrization

from sqlno.athena import show_partitions, alter_table, partition, s
from sqlno.common.structures import db, c

TEST_TABLE_NAME_0 = 't_0'
TEST_DATABASE_NAME_0 = 'db_0'
TEST_DATABASE_0 = db(TEST_DATABASE_NAME_0)

COLUMN_0 = c('c_0')
COLUMN_1 = c('c_1')
PARTITION_0 = partition(COLUMN_0 == s('0'), COLUMN_1 == s('0'))
PARTITION_1 = partition(COLUMN_0 == s('1'), COLUMN_1 == s('1'))


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name='',
    expected_query='SHOW PARTITIONS t_0;',
    actual_query=show_partitions(TEST_TABLE_NAME_0).semicolon()
)
@Parametrization.case(
    name='',
    expected_query="ALTER TABLE db_0.t_0 DROP "
                   "PARTITION (c_0 = '0', c_1 = '0'), PARTITION (c_0 = '1', c_1 = '1');",
    actual_query=alter_table(TEST_DATABASE_0.t_0).drop(PARTITION_0, PARTITION_1).semicolon()
)
@Parametrization.case(
    name='',
    expected_query="ALTER TABLE db_0.t_0 DROP "
                   "IF EXISTS "
                   "PARTITION (c_0 = '0', c_1 = '0'), PARTITION (c_0 = '1', c_1 = '1');",
    actual_query=alter_table(TEST_DATABASE_0.t_0).drop_if_exists(PARTITION_0, PARTITION_1).semicolon()
)
def test_expressions(expected_query, actual_query):
    assert str(actual_query) == expected_query
