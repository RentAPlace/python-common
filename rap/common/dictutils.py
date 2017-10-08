def merge(a, b):
    """ Merges two dictionaries into a new one.

    Args:
        a (dict): The first dictionary.
        b (dict): The second dictionary.

    Returns:
        dict: A new dictionary updated with the values of the given dictionaries.
    """
    result = a.copy()
    result.update(b)
    return result
