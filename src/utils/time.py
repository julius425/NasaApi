import functools
import time


def timeit(f):
    """
    секундомер
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print(f'{time.time() - start}')
        return result
    return wrapper
