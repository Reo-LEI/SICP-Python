# from sympy import *  # sympy 不能将运算符符号化，改用字符（eg： ‘a'）替代符号
from orderedPair import *

__all__ = ['ql', 'eq', 'memq', 'symt', 'eql']


def quote_list(seq):
    if seq is None:
        return None
    else:
        return cons(str(car(seq)), quote_list(cdr(seq)))


def equal(sy1, sy2):
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


def symbol_test(sy):
    if isinstance(sy, (str, int, float)):
        return True
    else:
        return False


def equal_list(seq1, seq2):
    if symt(seq1) and symt(seq2):
        if eq(seq1, seq2):
            return True
        else:
            return False
    elif seq1 is None and seq2 is None:
        return True
    elif eq(car(seq1), car(seq2)):
        return equal_list(cdr(seq1), cdr(seq2))
    else:
        return False


ql = quote_list
eq = equal
symt = symbol_test
eql = equal_list


if __name__ == '__main__':
    l1 = lister(1, 2, 3)
    l2 = lister(4, 5, 6)
    l3 = lister(7, 8, 9)
    ll = lister(l1, l2, l3)

    display(ql(l1))
    display(ql(ll))
    display(car(ql(ll)))
    display(cdr(ql(ll)))
    display(car(cdr(ql(ll))))
    print(type(car(cdr(ql(ll)))), '\n')
    display(eql('a', 'b'))
