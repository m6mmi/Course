from datetime import datetime
from time import time


def run_begin_after(func):
    def wrapper():
        t_start = time()
        print('Start', t_start)
        func()
        t_end = time()
        print('End', t_end)
        print(f'Run time = {(t_end - t_start):.2f}')
    return wrapper


@run_begin_after
def say_hello():
    for i in range(99999999):
        pass
    print('Function to measure')


say_hello()
