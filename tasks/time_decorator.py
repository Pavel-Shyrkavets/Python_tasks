from typing import Dict
from datetime import datetime

execution_time: Dict[str, int] = {}

def time_decorator(func):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """

    def wrapper(a, b):
        start = datetime.now()
        total = func(a, b)
        end = datetime.now()
        diff = end - start
        execution_time[func.__name__] = diff.microseconds
        return total
    return wrapper

def print_execution_time():
    print(f"Execution time in microseconds: {execution_time}")
