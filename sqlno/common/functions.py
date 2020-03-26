class Function(object):
    def __init__(self, function_name, *arguments):
        self.function_name = function_name
        self.arguments = arguments

    def __str__(self):
        return '{}({})'.format(self.function_name, ', '.join(map(str, self.arguments)))


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


class ParseDatetime(Function):
    def __init__(self, datetime_value, datetime_format):
        super(ParseDatetime, self).__init__('PARSE_DATETIME', datetime_value, datetime_format)


class SubStr(Function):
    def __init__(self, value, start, length):
        super(SubStr, self).__init__('SUBSTR', value, start, length)
