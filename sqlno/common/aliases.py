from six.moves import reduce

from sqlno.common.expressions import (
    Assignment, AtMostOperator, Parenthesize, IsNotOperator, NotEqualOperator, AndOperator, GreaterThenOperator,
    IsOperator, OrOperator, ConditionCaseExpression, CompareCaseExpression,
    ConcatOperator,
    Stringifies,
    EqualOperator,
)

# consts
ASTRIX = '*'
NULL = 'NULL'

# expression
SET = Assignment
p = Parenthesize
s = Stringifies

# boolean operators
AND = AndOperator
OR = OrOperator

# identity operators
is_ = IsOperator
IS_NOT = IsNotOperator

# comparison operators
eq = EqualOperator
NE = NotEqualOperator
GT = GreaterThenOperator
GTE = AtMostOperator

# control flow functions
CASE = CompareCaseExpression.create
case_when = ConditionCaseExpression.create


def concat(*operands):
    return reduce(ConcatOperator, operands)


