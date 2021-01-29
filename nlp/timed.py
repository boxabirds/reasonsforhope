# timing

import time
from functools import wraps
import logging

log = logging.getLogger()

def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        log.info(",{},{}".format(func.__name__, round(end - start, 4)))
        return result

    return wrapper
