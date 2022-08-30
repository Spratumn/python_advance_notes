from functools import singledispatch
from icecream import ic


@singledispatch
def multiply(arg1, arg2):
    return arg1 * arg2

@multiply.register
def _(arg1: str, arg2: str): return int(arg1) * arg2

@multiply.register
def _(arg1: int, arg2: int):
    return arg1 * arg2

@multiply.register
def _(arg1: list, arg2: list):
    assert len(arg1) == len(arg2)
    return [a1 * a2 for a1, a2 in zip(arg1, arg2)]

@multiply.register
def _(arg1: int, arg2: str):
    return arg1 * arg2



ic(multiply(3, 'test'))  #'testtesttest'
ic(multiply([3, 4, 5], [4, 5, 6])) # [12, 20, 30]
ic(multiply('4', 'test')) # 'testtesttesttes'
ic(multiply(3, 4))  # 12
ic(multiply(3, [3, 4, 5])) # [3, 4, 5, 3, 4, 5, 3, 4, 5]