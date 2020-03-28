from sqlno.common.expressions import Expression as _Expression


def _format_arguments(*arguments):
    return ', '.join(map(str, arguments))


def _format_function(name, arguments_expression):
    return _Expression('{}({})'.format(name, arguments_expression))


def _format_comma_separated_arguments_function(name, *arguments):
    return _Expression('{}({})'.format(name, _format_arguments(*arguments)))


def values(column_name):
    return _format_comma_separated_arguments_function('values', column_name)


def if_(condition, truth_value, faulty_value):
    return _format_comma_separated_arguments_function(
        'if', condition, truth_value, faulty_value
    )


def coalesce(value, *rest_of_values):
    return _format_comma_separated_arguments_function(
        'coalesce', value, *rest_of_values
    )


def current_timestamp():
    return _format_comma_separated_arguments_function(
        'current_timestamp'
    )


def substr(string, start, length):
    return _format_comma_separated_arguments_function(
        'substr', string, start, length
    )
