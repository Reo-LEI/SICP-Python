from sympy import *
from orderedpair import *


def quote(symbol):
    symbol = Symbol('symbol')
    return symbol


def eq(sy1, sy2):
    if sy1 == sy2:
        return True
    else:
        return False


def memq(sy, seq):
    if seq is None:
        return False
    elif eq(sy, car(seq)):
        return seq
    else:
        return memq(sy, cdr(seq))


