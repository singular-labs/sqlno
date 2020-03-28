from sqlno.common.functions import _format_comma_separated_arguments_function, _format_function


def parse_datetime(value, format_):
    return _format_comma_separated_arguments_function(
        'parse_datetime', value, format_
    )


def replace(string, pattern, replacement):
    return _format_comma_separated_arguments_function(
        'replace', string, pattern, replacement
    )


def url_extract_parameter(url, parameter):
    return _format_comma_separated_arguments_function(
        'url_extract_parameter', url, parameter
    )


def trim(string):
    return _format_comma_separated_arguments_function(
        'trim', string
    )


def json_extract_scalar(json_string, json_query):
    return _format_comma_separated_arguments_function(
        'json_extract_scalar', json_string, json_query
    )


def lower(string):
    return _format_comma_separated_arguments_function(
        'lower', string
    )


def cast(expression, as_):
    return _format_function(
        'cast', '{} AS {}'.format(expression, as_)
    )


def length(string):
    return _format_comma_separated_arguments_function(
        'length', string
    )


def greatest(*values):
    return _format_comma_separated_arguments_function(
        'greatest', *values
    )


def floor(value):
    return _format_comma_separated_arguments_function(
        'floor', value
    )


def to_unixtime(value):
    return _format_comma_separated_arguments_function(
        'to_unixtime', value
    )


def from_unixtime(value):
    return _format_comma_separated_arguments_function(
        'from_unixtime', value
    )


def date(value):
    return _format_comma_separated_arguments_function(
        'date', value
    )


def at_timezone(timestamp, timezone):
    return _format_comma_separated_arguments_function(
        'at_timezone', timestamp, timezone
    )


def sum_(*values):
    return _format_comma_separated_arguments_function(
        'sum', *values
    )
