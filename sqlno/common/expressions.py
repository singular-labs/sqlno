import attr


class Assignment(object):
    def __init__(self, column_name, value_expression):
        self.column_name = column_name
        self.value_expression = value_expression

    def __str__(self):
        return '{} = {}'.format(self.column_name, self.value_expression)


class Expression(object):
    __slots__ = 'value',

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return SubtractOperator(self.value, other)

    def __div__(self, other):
        return DivisionOperator(self.value, other)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return EqualOperator(self.value, other)

    def __ne__(self, other):
        return NotEqualOperator(self.value, other)

    def and_(self, other):
        return AndOperator(self.value, other)

    def is_(self, other):
        return IsOperator(self.value, other)

    def is_not(self, other):
        return IsNotOperator(self.value, other)

    def not_in(self, other):
        return NotInOperator(self.value, other)

    def __le__(self, other):
        return AtLeastOperator(self.value, other)

    def __lt__(self, other):
        return LessThenOperator(self.value, other)

    def __gt__(self, other):
        return GreaterThenOperator(self.value, other)


e = Expression


def array(*values):
    return Expression('({})'.format(', '.join(values)))


a = array


class BinaryOperator(Expression):
    OPERATOR = None

    def __init__(self, left, right):
        value = '{} {} {}'.format(left, self.OPERATOR, right)
        super(BinaryOperator, self).__init__(value)


class DivisionOperator(BinaryOperator):
    OPERATOR = '/'


class NotInOperator(BinaryOperator):
    OPERATOR = 'NOT IN'


class ConcatOperator(BinaryOperator):
    OPERATOR = '||'


class GreaterThenOperator(BinaryOperator):
    OPERATOR = '>'


class LessThenOperator(BinaryOperator):
    OPERATOR = '<'


class AtMostOperator(BinaryOperator):
    OPERATOR = '>='


class AtLeastOperator(BinaryOperator):
    OPERATOR = '<='


class EqualOperator(BinaryOperator):
    OPERATOR = '='


class NotEqualOperator(BinaryOperator):
    OPERATOR = '!='


def parenthesize(expression):
    return Expression('({})'.format(expression))


p = parenthesize


def stringifies(string):
    return Expression("'{}'".format(string))


s = stringifies


class IsNotOperator(BinaryOperator):
    OPERATOR = 'IS NOT'


class AndOperator(BinaryOperator):
    OPERATOR = 'AND'


class OrOperator(BinaryOperator):
    OPERATOR = 'OR'


class IsOperator(BinaryOperator):
    OPERATOR = 'IS'


class SubtractOperator(BinaryOperator):
    OPERATOR = '-'


@attr.s()
class ConditionWhenTuple(object):
    condition = attr.ib()
    result = attr.ib()

    def __str__(self):
        return 'WHEN {} THEN {}'.format(self.condition, self.result)


@attr.s()
class CompareWhenTuple(object):
    compare_value = attr.ib()
    result = attr.ib()

    def __str__(self):
        return 'WHEN {} THEN {}'.format(self.compare_value, self.result)


class CaseContext(object):
    def __init__(self, when_tuples=None, else_result=None):
        self.when_tuples = when_tuples or []
        self.else_result = else_result

    def _get_case(self):
        raise NotImplementedError()

    def end(self):
        expression = self._get_case()
        expression += ' '.join(
            [str(when_tuple) for when_tuple in self.when_tuples]
        )
        if self.else_result is not None:
            expression += ' ELSE {}'.format(self.else_result)
        expression += ' END'
        return expression


class ConditionCaseContext(CaseContext):
    def _get_case(self):
        return 'CASE '


class CompareCaseContext(CaseContext):
    def __init__(self, value, when_tuples=None, else_result=None):
        self.value = value
        super(CompareCaseContext, self).__init__(when_tuples, else_result)

    def _get_case(self):
        return 'CASE {} '.format(self.value)


class ConditionCaseExpression(object):
    def __init__(self, context):
        # type: (ConditionCaseContext) -> None
        self.context = context

    def when(self, compare_value):
        return ConditionWhenExpression(self.context, compare_value)


def case_when(condition):
    return ConditionWhenExpression(ConditionCaseContext(), condition)


class CompareCaseExpression(object):
    def __init__(self, context):
        # type: (CompareCaseContext) -> None
        self.context = context

    def when(self, compare_value):
        return CompareWhenExpression(self.context, compare_value)


def case(expression):
    return CompareCaseExpression(CompareCaseContext(expression))


class SatisfyingCompareCaseExpression(CompareCaseExpression):
    def else_(self, result):
        self.context.else_result = result
        return self.context

    def end(self):
        return self.context.end()


class SatisfyingConditionCaseExpression(ConditionCaseExpression):
    def else_(self, result):
        self.context.else_result = result
        return self.context

    def end(self):
        return self.context.end()


class ConditionWhenExpression(object):
    def __init__(self, context, condition):
        self.context = context
        self.condition = condition

    def then(self, result):
        self.context.when_tuples.append(ConditionWhenTuple(self.condition, result))
        return SatisfyingConditionCaseExpression(self.context)


class CompareWhenExpression(object):
    def __init__(self, context, compare_value):
        self.context = context
        self.compare_value = compare_value

    def then(self, result):
        self.context.when_tuples.append(CompareWhenTuple(self.compare_value, result))
        return SatisfyingCompareCaseExpression(self.context)
