import numpy as np


####### mutable ############

# list, dict, ndarray

def edit_list(ls:list):
    ls.append(1)

a = [0]
print(a)
edit_list(a)
print(a)


def edit_dict(dt:dict):
    dt['new_key'] = 1

b = {'1': 1}
print(b)
edit_dict(b)
print(b)


def edit_ndarray1(ndary:np.ndarray):
    ndary[0, 0] = 1

c = np.zeros((5, 5))
print(c)
edit_ndarray1(c)
print(c)


def edit_tuple(tp:tuple):
    tp[0][0] = 1

d = ([0, 0], 5)
print(d)
edit_tuple(d)
print(d)


####### unmutable ############

# num_var, tuple

def edit_num(n:int or float):
    n = 1

e = 0
print(e)
edit_num(e)
print(e)


def edit_ndarray2(ndary:np.ndarray):
    ndary = ndary[:3, :2]

f = np.zeros((5, 5))
print(f)
edit_ndarray2(f)
print(f)
