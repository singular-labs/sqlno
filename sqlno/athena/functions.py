from ..common.functions import *


class ParseDatetimeFunction(Function):
    def __init__(self, datetime_value, datetime_format):
        super(ParseDatetimeFunction, self).__init__('parse_datetime', datetime_value, datetime_format)


class ReplaceFunction(Function):
    def __init__(self, string, pattern, replacement):
        super(ReplaceFunction, self).__init__('replace', string, pattern, replacement)


class UrlExtractParameterFunction(Function):
    def __init__(self, url, parameter):
        super(UrlExtractParameterFunction, self).__init__('url_extract_parameter', url, parameter)


class TrimFunction(Function):
    def __init__(self, string):
        super(TrimFunction, self).__init__('trim', string)


class JsonExtractScalarFunction(Function):
    def __init__(self, json_string, json_query):
        super(JsonExtractScalarFunction, self).__init__('json_extract_scalar', json_string, json_query)


class LowerFunction(Function):
    def __init__(self, string):
        super(LowerFunction, self).__init__('lower', string)


class CastFunction(Function):
    def __init__(self, expression, cast_type):
        super(CastFunction, self).__init__('cast', expression, cast_type)

    @property
    def arguments_expression(self):
        return '{} AS {}'.format(*map(str, self.arguments))


class LengthFunction(Function):
    def __init__(self, string):
        super(LengthFunction, self).__init__('length', string)


parse_datetime = ParseDatetimeFunction
replace = ReplaceFunction
url_extract_parameter = UrlExtractParameterFunction
trim = TrimFunction
json_extract_scalar = JsonExtractScalarFunction
cast = CastFunction
lower = LowerFunction
length = LengthFunction
