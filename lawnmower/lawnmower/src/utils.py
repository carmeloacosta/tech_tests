def get_bool_from_str(input_str):
    """
        Translates the input string into a boolean variable, returning its value.

    :param input_str: (str) The string to convert to boolean.
    :return: (bool) The translation of the string to boolean value.
    """
    result = False

    if input_str in ["t", "T", "True", "Yes", "y", "Y", "1"]:
        result = True

    return result
