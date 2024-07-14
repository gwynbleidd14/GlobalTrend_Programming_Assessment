'''
7. Write a Python decorator that measures the execution time of a function and logs it.
Apply this decorator to a function that performs a computationally expensive task.
'''

import time
import logging
import sys

sys.set_int_max_str_digits(100000)
logging.basicConfig(level=logging.INFO)

def measure(fx):
    def mfx(*args, **kwargs):
        start = time.time()
        res = fx(*args, **kwargs)
        end = time.time()
        exe_time = end - start
        logging.info(f"Function {fx.__name__} executed in {exe_time:.4f} seconds")
        return res
    return mfx

@measure
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5000))
