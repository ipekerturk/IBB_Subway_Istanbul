import time

def measure_runtime(function, *args):
    start = time.perf_counter()
    result = function(*args)
    end = time.perf_counter()

    return result, end - start