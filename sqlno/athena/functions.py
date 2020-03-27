from sqlno.common.functions import Function


class ParseDatetimeFunction(Function):
    NAME = 'parse_datetime'

    def __call__(self, datetime_value, datetime_format):
        return super(ParseDatetimeFunction, self).__call__(datetime_value, datetime_format)


class ReplaceFunction(Function):
    NAME = 'replace'

    def __call__(self, string, pattern, replacement):
        return super(ReplaceFunction, self).__call__(string, pattern, replacement)


class UrlExtractParameterFunction(Function):
    NAME = 'url_extract_parameter'

    def __call__(self, url, parameter):
        return super(UrlExtractParameterFunction, self).__call__(url, parameter)


class TrimFunction(Function):
    NAME = 'trim'

    def __call__(self, string):
        return super(TrimFunction, self).__call__(string)


class JsonExtractScalarFunction(Function):
    NAME = 'json_extract_scalar'

    def __call__(self, json_string, json_query):
        return super(JsonExtractScalarFunction, self).__call__(json_string, json_query)


class LowerFunction(Function):
    NAME = 'lower'

    def __call__(self, string):
        return super(LowerFunction, self).__call__(string)


class CastFunction(Function):
    NAME = 'cast'

    def __call__(self, expression, as_):
        return super(CastFunction, self).__call__(expression, as_)

    @classmethod
    def format_arguments_expression(cls, *arguments):
        return '{} AS {}'.format(*map(str, arguments))


class LengthFunction(Function):
    NAME = 'length'

    def __call__(self, string):
        return super(LengthFunction, self).__call__(string)


class GreatestFunction(Function):
    NAME = 'greatest'

    def __call__(self, *values):
        return super(GreatestFunction, self).__call__(*values)


class FloorFunction(Function):
    NAME = 'floor'

    def __call__(self, value):
        return super(FloorFunction, self).__call__(value)


class ToUnixTimeFunction(Function):
    NAME = 'to_unixtime'

    def __call__(self, value):
        return super(ToUnixTimeFunction, self).__call__(value)
