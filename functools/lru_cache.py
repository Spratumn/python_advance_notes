from functools import lru_cache

from time import time


@lru_cache(maxsize=2**10)
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1

start = time()
print(fib(100))
print(time() - start)