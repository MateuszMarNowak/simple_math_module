from functools import reduce

def power(*args):
    return reduce(lambda x, y: x ^ y, args)