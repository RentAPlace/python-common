import concurrent.futures

PROCESS = concurrent.futures.ProcessPoolExecutor
THREAD  = concurrent.futures.ThreadPoolExecutor


def dexecute(func, iterable, *args, **kwargs):
    """ Runs the given function for every object in iterable.

    Has the same interface as `pexecute` and `texecute`, serves as a debugging tool.

    Args:
        func (function): The function to run.
        iterable (iterable[object]): The elements passed to the function.
        *args: Variable length argument list `func` is applied to.
        **kwargs: Arbitrary keyword arguments `func` is applied to.

    Returns:
        None
    """
    for elem in iterable:
        func(elem, *args, **kwargs)


def pexecute(func, iterable, *args, **kwargs):
    """ Runs the given function in parallel (with processes) for every object in iterable.

    `func` is applied to every element in `iterable`, and is also passed `*args`
    and `**kwargs`. The result of `func` is discarded. Use ``concurrent.futures.map``
    if the result is to be kept.

    Args:
        func (function): The function to run in parallel.
        iterable (iterable[object]): The elements passed to the function.
        *args: Variable length argument list `func` is applied to.
        **kwargs: Arbitrary keyword arguments `func` is applied to.

    Returns:
        None
    """
    __execute(func, iterable, PROCESS, *args, **kwargs)


def texecute(func, iterable, *args, **kwargs):
    """ Runs the given function in parallel (with threads) for every object in iterable.

    `func` is applied to every element in `iterable`, and is also passed `*args`
    and `**kwargs`. The result of `func` is discarded. Use ``concurrent.futures.map``
    if the result is to be kept.

    Args:
        func (function): The function to run in parallel.
        iterable (iterable[object]): The elements passed to the function.
        *args: Variable length argument list `func` is applied to.
        **kwargs: Arbitrary keyword arguments `func` is applied to.

    Returns:
        None
    """
    __execute(func, iterable, THREAD, *args, **kwargs)


def __execute(func, iterable, executor, *args, **kwargs):
    with executor() as e:
        futures = list(e.submit(func, elem, *args, **kwargs) for elem in iterable)
        concurrent.futures.wait(futures)
