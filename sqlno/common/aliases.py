from sqlno.common.expressions import (
    Assignment, AtMostOperator, Parenthesize, IsNotOperator, NotEqualOperator, AndOperator, GreaterThenOperator,
    IsOperator, OrOperator, ConditionCaseExpression, CompareCaseExpression,
    ConcatOperator,
)

# consts
ASTRIX = '*'
NULL = 'NULL'

# expression
SET = Assignment
P = Parenthesize

# boolean operators
AND = AndOperator
OR = OrOperator

# identity operators
IS = IsOperator
IS_NOT = IsNotOperator

# comparison operators
NE = NotEqualOperator
GT = GreaterThenOperator
GTE = AtMostOperator

# control flow functions
CASE = CompareCaseExpression.create
CASE_WHEN = ConditionCaseExpression.create

CONCAT = ConcatOperator
