from __future__ import division  # That operator '/' did not work as '//'
__author__ = 'Mihail Perminov <PerminovMA@live.ru>'

ERROR_STRING = 'ERROR'

def check_correctness_expression(expression):
    """ Check the correctness of expression.
    :param string expression: expression to check (for example: '5+5')
    :return boolean: check result (for example: True)

    """

    AVAILABLE_CHARACTERS = '0123456789-+*/e,.'
    UNAVAILABLE_CHARACTER_COMBINATIONS = ['**', '//', '--', '++', ',,', '..']

    if type(expression) is not str:
        return False  # Expression is not string

    if len(expression) > 100:
        return False  # Expression is too long

    for character in expression:
        if character not in AVAILABLE_CHARACTERS:
            return False  # Expression contains invalid characters

    for combination in UNAVAILABLE_CHARACTER_COMBINATIONS:
        if combination in expression:
            return False  # Expression contains invalid character combinations

    return True


def calculate_expression(expression):
    """ Calculates the expression.
    :param string expression: expression to calculate (for example: '5+5')
    :return string: answer (for example '10')

    If an error occurs, function will return ERROR_STRING

    """

    if not expression:
        return ''

    if not check_correctness_expression(expression):
        return ERROR_STRING

    expression = expression.replace(',', '.')  # Python uses the dot as separator for numbers

    try:
        result = eval(expression, {'__builtins__': {}})  # Calculation
    except (ZeroDivisionError, SyntaxError):
        return ERROR_STRING

    # in order to a number is displayed without a point (for example 3.0 as 3)
    if type(result) is float and result.is_integer():
        result = int(result)

    result = str(result).replace('.', ',')

    return result