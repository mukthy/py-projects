from time import time
from unittest import result


def performance_time(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} secs')
        return result
    return wrapper


@performance_time
def long_time():
    for i in range(100000000):
        i*5


long_time()
