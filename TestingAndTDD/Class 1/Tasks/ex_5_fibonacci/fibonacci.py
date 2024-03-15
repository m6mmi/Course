# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
from functools import lru_cache

@lru_cache(None)
def fibonacci(n: int) -> int:
    if n < 0:
        print("Incorrect input")
    elif n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"10 = {fibonacci(10)}")
    print(f"2 = {fibonacci(2)}")
    print(f"5 = {fibonacci(5)}")
    print(f"100 = {fibonacci(100)}")
