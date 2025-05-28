from time import sleep
from typing import Dict
from datetime import datetime

execution_time: Dict[str, float] = {}

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
        execution_time[func.__name__] = float(diff.total_seconds())
        return total
    return wrapper

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

#x, y = 10, 20
#result = func_add(x, y)
#print(f"{x} + {y} = {result}")
#print(f"Execution time: {execution_time['func_add']} seconds")
