from datetime import datetime


def run_begin_after(func):
    def wrapper():
        print(datetime.today().time())
        result = func()
        print(datetime.today().time())
        return result
    return wrapper


@run_begin_after
def say_hello():
    for i in range(100000):
        pass
    print('Hello')


say_hello()
