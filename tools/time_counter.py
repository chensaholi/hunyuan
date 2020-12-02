import time


def calc_time_interval(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        interval = time.time() - start
        print("the time interval: %s s", round(interval, 2))
        return res
    return wrapper
