from time import sleep
from typing import Dict
import datetime

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """

    def wrapper(a, b, sleep_time):
        start = datetime.datetime.now()
        sleep(sleep_time)
        total = fn(a, b, sleep_time)
        end = datetime.datetime.now()
        diff = end - start
        execution_time[fn.__name__] = float(diff.total_seconds())
        return total
    return wrapper
