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
        if isinstance(other, Expression):
            return EqualOperator(other, self.value)
        return EqualOperator(self.value, other)

    def and_(self, other):
        return AndOperator(self.value, other)


class BinaryOperator(Expression):
    OPERATOR = None

    def __init__(self, left, right):
        super(BinaryOperator, self).__init__('{} {} {}'.format(left, self.OPERATOR, right))


class DivisionOperator(BinaryOperator):
    OPERATOR = '/'


class ConcatOperator(BinaryOperator):
    OPERATOR = '||'


class GreaterThenOperator(BinaryOperator):
    OPERATOR = '>'


class AtMostOperator(BinaryOperator):
    OPERATOR = '>='


class EqualOperator(BinaryOperator):
    OPERATOR = '='


class NotEqualOperator(BinaryOperator):
    OPERATOR = '!='


class Parenthesize(Expression):
    def __init__(self, expression):
        super(Parenthesize, self).__init__('({})'.format(expression))


class Stringifies(Expression):
    def __init__(self, string):
        super(Stringifies, self).__init__("'{}'".format(string))


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


@attr.s()
class ConditionCaseContext(CaseContext):
    when_tuples = attr.ib(default=[])
    else_result = attr.ib(default=None)

    def _get_case(self):
        return 'CASE '


@attr.s()
class CompareCaseContext(CaseContext):
    value = attr.ib()
    when_tuples = attr.ib(default=[])
    else_result = attr.ib(default=None)

    def _get_case(self):
        return 'CASE {} '.format(self.value)


class ConditionCaseExpression(object):
    def __init__(self, context):
        # type: (ConditionCaseContext) -> None
        self.context = context

    def when(self, compare_value):
        return ConditionWhenExpression(self.context, compare_value)

    @classmethod
    def create(cls, condition):
        return ConditionCaseExpression(ConditionCaseContext()).when(condition)


class CompareCaseExpression(object):
    def __init__(self, context):
        # type: (CompareCaseContext) -> None
        self.context = context

    def when(self, compare_value):
        return CompareWhenExpression(self.context, compare_value)

    @classmethod
    def create(cls, value):
        return CompareCaseExpression(CompareCaseContext(value))


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
    def __init__(self, context, compare_value):
        self.context = context
        self.condition = compare_value

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
