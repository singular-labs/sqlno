from six.moves import reduce

from sqlno.common.expressions import (
    Assignment, AtMostOperator, p, IsNotOperator, NotEqualOperator, AndOperator, GreaterThenOperator,
    IsOperator, OrOperator, ConcatOperator, s, EqualOperator,
)

# consts
astrix = '*'
NULL = 'NULL'

# expression
set_ = Assignment


# boolean operators
def and_(*operands):
    return reduce(AndOperator, operands)


def or_(*operands):
    return reduce(OrOperator, operands)


# identity operators
is_ = IsOperator
is_not = IsNotOperator

# comparison operators
eq = EqualOperator
ne = NotEqualOperator
gt = GreaterThenOperator
gte = AtMostOperator


def concat(*operands):
    return reduce(ConcatOperator, operands)


# types
INTEGER = 'INTEGER'
BIGINT = 'BIGINT'
