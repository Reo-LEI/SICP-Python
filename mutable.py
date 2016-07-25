from orderedPair import display

__all__ = ['eq', 'memq', 'cons', 'car', 'cdr', 'set_car', 'set_cdr',
           'display_pair']


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


def cons(x, y):
    def set_x(v):
        nonlocal x
        x = v

    def set_y(v):
        nonlocal y
        y = v

    def dispatch(m):
        if m == 'car':
            return x
        elif m == 'cdr':
            return y
        elif m == 'set_car':
            return set_x
        elif m == 'set_cdr':
            return set_y
        else:
            return 'error, Undefined operation -- CONS'
    return dispatch


def car(z):
    return z('car')


def cdr(z):
    return z('cdr')


def set_car(z, v):
    z('set_car')(v)
    return z


def set_cdr(z, v):
    z('set_cdr')(v)
    return z


def display_pair(p):
    def inner(z):
        if z is None or isinstance(z, (str, int, float)):
            return z
        else:
            return (inner(car(z)), inner(cdr(z)))
    result = inner(p)
    print(result, '\n')
    # display(result)
    return result

if __name__ == '__main__':
    p1 = cons(1, 2)
    p2 = cons(3, 4)
    p3 = cons(5, 6)

    display_pair(p1)
    display_pair(p2)
    display_pair(p3)
    display_pair(car(p1))
    display_pair(cdr(p1))
    display_pair(set_car(p1, p2))
    display_pair(car(set_car(p1, p2)))




