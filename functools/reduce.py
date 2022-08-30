from functools import reduce
import operator as op
from icecream import ic


def merge(nested):
    """
    :param nested: a list which contains lots of lists
    :return: a single list, which concat the lists.
    """
    type_op = {
        list: op.add,
        int: op.add,
        float: op.add,
        set: op.or_,
        str: op.add
    }
    if nested:
        element = nested[0]
        return reduce(type_op[type(element)], nested)
    else:
        return nested


some_lists = [
    [1, 2],
    [3, 5],
    [5, 6, 7, 1, 10.1, 11.1],
    [121.4, 11.34],
    [11.31, 1921, 321.],
]

some_sets = (
    {'1', '2'},
    {'some_node', 'node_2'},
    {'action_1', 'node_2'},
    {'id_x'}
)

some_files = [
    'file_01',
    'file_02',
    'file_03',
    'file_01',
    'file_02',
    'file_03',
    'file_01',
    'file_02',
    'file_03',
    'file_01',
    'file_02',
    'file_03'
]

ic(merge(some_lists))
ic(merge(some_sets))
ic(merge(some_files))
ic(merge(['string1', 'string2', 'string3', 'string4']))
ic(merge([]))
ic(merge(None))