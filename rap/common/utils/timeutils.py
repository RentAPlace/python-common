import time


def timeit(func, *args, **kwargs):
    """ Gets the time spent on executing the given function in seconds.

    Args:
        func (function): The function to execute.
        *args: Variable length argument list expanded in `func`.
        **kwargs: Keyword arguments expanded in `func`.

    Returns:
        tuple: A tuple containing:
            timespan (float): The timespan of `func` execution.
            return_value (object): The return value of `func`.
    """
    start  = time.time()
    result = func(*args, **kwargs)
    return (time.time() - start, result)
