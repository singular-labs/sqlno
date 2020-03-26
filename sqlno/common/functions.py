class Function(object):
    def __init__(self, function_name, *arguments):
        self.function_name = function_name
        self.arguments = arguments

    @property
    def arguments_expression(self):
        return ', '.join(map(str, self.arguments))

    def __str__(self):
        return '{}({})'.format(self.function_name, self.arguments_expression)


class Values(Function):
    def __init__(self, column_name):
        super(Values, self).__init__('VALUES', column_name)


class If(Function):
    def __init__(self, condition, truth_value, faulty_value):
        super(If, self).__init__('IF', condition, truth_value, faulty_value)


class Coalesce(Function):
    def __init__(self, value, *rest_of_values):
        super(Coalesce, self).__init__('COALESCE', value, *rest_of_values)


class CurrentTimestamp(Function):
    def __init__(self):
        super(CurrentTimestamp, self).__init__('CURRENT_TIMESTAMP')


class SubStrFunction(Function):
    def __init__(self, value, start, length):
        super(SubStrFunction, self).__init__('substr', value, start, length)


substr = SubStrFunction
coalesce = Coalesce
