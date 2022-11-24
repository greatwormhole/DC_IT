import time
import datetime
from inspect import getcallargs

logger = []

def time_decorator(func):

    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        print(round(time.time() - before))
        return value

    return wrapper

def logging_decorator(__list):

    def decorator(func):

        def wrapper(*args, **kwargs):
            time = datetime.datetime.now()
            res = func(*args, **kwargs)
            __list.append({"name": func.__name__,
                           "arguments": getcallargs(func, *args, **kwargs),
                           "call_time": time,
                           "result": res})
            return res

        return wrapper

    return decorator
