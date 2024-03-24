from datetime import datetime

""" Simple decorator """
# def disable_at_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#
#     return wrapper
#
#
# @disable_at_night
# def say_something():
#     print("Hello world")
#
#
# say_something()

""" Decorator with parameters """
def run_only_between(from_=7, to_=22):
    def dec(func):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                func(*args, **kwargs)

        return wrapper

    return dec


@run_only_between(9, 15)
def say_something_1():
    print("Hello world")


@run_only_between(10, 21)
def say_something_2():
    print("Hello room")


say_something_1()
say_something_2()
