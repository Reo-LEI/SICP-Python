from orderedPair import *
from symbolic import *


# 2.53
display(lister('a', 'b', 'c'))
display(lister(lister('george')))
display(ql(lister(lister('x1', 'x2'), lister('y1', 'y2'))))
print(isinstance(car(ql(lister('a', 'short', 'list'))), tuple), '\n')
display(memq('red', ql(lister(lister('red', 'shoes'), lister('blue', 'socks')))))
display(memq('red', ql(lister('red', 'shoes', 'blue', 'socks'))))


# 2.54
def equal(seq1, seq2):
    def symbol_test(sy):
        if isinstance(sy, str):
            return True
        else:
            return False
    if symbol_test(seq1) and symbol_test(seq2):
        if eq(seq1, seq2):
            return True
        else:
            return False
    elif seq1 is None and seq2 is None:
        return True
    elif eq(car(seq1), car(seq2)):
        return equal(cdr(seq1), cdr(seq2))
    else:
        return False


# 2.55
print(car('ql''abracadabra'))


if __name__ == '__main__':
    print(equal(lister(1, 2, 3), lister(1, 2, 3)))
    print(equal(lister(1, 2, 3), lister(1, lister(2), 3)))

