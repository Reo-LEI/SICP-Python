from orderedPair import *

# 3.12
# response = (b, None)
# response = (b, (c, (d, None)))

# 3.13
# ('a', ('b', ('c', ('a', ('b', ('c', ('a', ('b', ('c',...

# 3.14
# v = ('a', ('b', ('c', None)))
# w = ('c', ('b', ('a', None)))


# 3.17
def eq(sy1, sy2):
    if sy1 is sy2:
        return True
    else:
        return False


def memq(sy, seq):
    if seq is None:
        return False
    elif eq(sy,car(seq)):
        return True
    else:
        return memq(sy, cdr(seq))


def count_pairs(x):
    memo_list = None

    def inner(k):
        nonlocal memo_list
        if not isinstance(k, tuple) or memq(k, memo_list):
            return 0
        else:
            cons(k, memo_list)
            return inner(car(k), memo_list) + inner(cdr(k), memo_list) + 1
    return inner(x)


# 3.18
def is_loop(lst):
    identity = cons(None, None)

    def iter(remain):
        nonlocal identity
        if remain is None:
            return False
        elif eq(identity,car(remain)):
            return True
        else:
            set_car(remain,identity)
            return iter(cdr(remain))
    return iter(lst)


# 3.19
def is_loop_new(lst):
    def list_walk(step, seq):
        if seq is None:
            return None
        elif not step:
            return seq
        else:
            return list_walk(step - 1, cdr(seq))

    def iter(x, y):
        xl = list_walk(1, seq)
        yl = list_walk(2, seq)
        if xl is None or yl is None:
            return False
        elif eq(xl, yl):
            return True
        else:
            return iter(xl, yl)
    return iter(lst, lst)




