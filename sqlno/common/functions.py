class Function(object):
    NAME = None

    @classmethod
    def format_arguments_expression(cls, *arguments):
        return ', '.join(map(str, arguments))

    def __call__(self, *arguments):
        return '{}({})'.format(self.NAME, self.format_arguments_expression(*arguments))


class ValuesFunction(Function):
    NAME = 'values'

    def __call__(self, column_name):
        return super(ValuesFunction, self).__call__(column_name)


class IfFunction(Function):
    NAME = 'if'

    def __call__(self, condition, truth_value, faulty_value):
        return super(IfFunction, self).__call__(condition, truth_value, faulty_value)


class CoalesceFunction(Function):
    NAME = 'coalesce'

    def __call__(self, value, *rest_of_values):
        return super(CoalesceFunction, self).__call__(value, *rest_of_values)


class CurrentTimestampFunction(Function):
    NAME = 'current_timestamp'

    def __call__(self):
        return super(CurrentTimestampFunction, self).__call__()


class SubStrFunction(Function):
    NAME = 'substr'

    def __call__(self, string, start, length):
        return super(SubStrFunction, self).__call__(string, start, length)


substr = SubStrFunction()
coalesce = CoalesceFunction()
if_ = IfFunction()
values = ValuesFunction()
current_timestamp = CurrentTimestampFunction()
