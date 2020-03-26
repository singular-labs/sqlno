from six.moves import reduce

from sqlno.common.expressions import (
    Assignment, AtMostOperator, Parenthesize, IsNotOperator, NotEqualOperator, AndOperator, GreaterThenOperator,
    IsOperator, OrOperator, ConditionCaseExpression, CompareCaseExpression,
    ConcatOperator,
    Stringifies,
    EqualOperator,
)

# consts
astrix = '*'
null = 'NULL'

# expression
set_ = Assignment
p = Parenthesize
s = Stringifies

# boolean operators
and_ = AndOperator
or_ = OrOperator

# identity operators
is_ = IsOperator
is_not = IsNotOperator

# comparison operators
eq = EqualOperator
ne = NotEqualOperator
gt = GreaterThenOperator
gte = AtMostOperator

# control flow functions
case = CompareCaseExpression.create
case_when = ConditionCaseExpression.create


def concat(*operands):
    return reduce(ConcatOperator, operands)


