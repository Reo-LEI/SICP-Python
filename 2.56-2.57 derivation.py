from orderedPair import *
from symbolic import *


def number(e):
    if isinstance(e, (int, float)):
        return True
    elif isinstance(e, str):
        if e.isdigit():
            return True
        else:
            return False
    else:
        return False


def variable(e):
    if symt(e):
        if e.isdigit():
            return False
        else:
            return True
    else:
        pass


def _make_sum(a1, a2):
    if a1 is '0':
        return a2
    elif a2 is '0':
        return a1
    elif symt(a1) and symt(a2):
        try:
            return str(int(a1) + int(a2))
        except ValueError:
            return lister(a1, '+', a2)
    else:
        return lister(a1, '+', a2)


def same_variable(v1, v2):
    if symt(v1) and symt(v2) and eq(v1, v2):
        return True
    else:
        return False


def sum_formula(f):
    if memq('+', f):
        return True
    else:
        return False


def addend(f):
    return car(f)


def augend(f):
    return car(cdr(cdr(f)))


def _make_product(m1, m2):
    if m1 is '0' or m2 is '0':
        return '0'
    elif m1 is '1':
        return m2
    elif m2 is '1':
        return m1
    elif symt(m1) and symt(m2):
        try:
            return str(int(m1) * int(m2))
        except ValueError:
            return lister(m1, '*', m2)
    else:
        return lister(m1, '*', m2)


def product_formula(f):
    if memq('*', f):
        return True
    else:
        return False


def multiplier(f):
    return car(f)


def multiplicand(f):
    return car(cdr(cdr(f)))


def deriv(exp, var):
    if number(exp):
        return '0'
    elif variable(exp):
        if same_variable(exp, var):
            return '1'
        else:
            return '0'
    elif sum_formula(exp):
        return make_sum(deriv(addend(exp), var),
                        deriv(augend(exp), var))
    elif product_formula(exp):
        return make_sum(
            make_product(multiplier(exp),
                         deriv(multiplicand(exp), var)),
            make_product(multiplicand(exp),
                         deriv(multiplier(exp), var)))
    elif exponentiation(exp):
        return make_product(exponent(exp),
                            make_product(
                                make_exponentiation(
                                    base(exp),
                                    make_sum(exponent(exp), '-1')),
                                deriv(base(exp), var)))
    else:
        return print('error, unknown expression type--Deriv')


# 2.56
def make_exponentiation(b, e):
    if e is '0':
        return '1'
    elif e is '1':
        return b
    elif symt(b) and symt(e):
        try:
            return str(int(b) ** int(e))
        except ValueError:
            return lister(b, '**', e)
    else:
        return lister(b, '**', e)


def exponentiation(f):
    if memq('**', f):
        return True
    else:
        return False


def base(f):
    return car(f)


def exponent(f):
    return car(cdr(cdr(f)))


# 2.57
def make_sum(*args):
    exp = lister(*args)

    def _sum(first, other):
        if other is None:
            return first
        elif first is '0':
            return _sum(other, cdr(other))
        elif car(other) is '0':
            return _sum(first, cdr(other))
        elif symt(first) and symt(car(other)):
            try:
                return _sum(str(int(first) + int(car(other))), cdr(other))
            except ValueError:
                return lister(first, '+', _sum(car(other), cdr(other)))
        else:
            return lister(first, '+', _sum(car(other), cdr(other)))
    return _sum(car(exp), cdr(exp))


def make_product(*args):
    exp = lister(*args)

    def _mul(first, other):
        if other is None:
            return first
        elif symt(first) and symt(car(other)):
            try:
                return _mul(str(int(first) * int(car(other))), cdr(other))
            except ValueError:
                return lister(first, '*', _mul(car(other), cdr(other)))
        else:
            return lister(first, '*', _mul(car(other), cdr(other)))
    if memq('0', exp):
        return '0'
    elif memq('1', exp):
        def picker(s):
            if s is None:
                return None
            elif eq(car(s), '1'):
                return picker(cdr(s))
            else:
                return cons(car(s), picker(cdr(s)))
        exp = picker(exp)
        return _mul(car(exp), cdr(exp))
    else:
        return _mul(car(exp), cdr(exp))


# 2.58 a, b
# 使用新版make_sum和make_product之后程序基本上能正确表示


if __name__ == '__main__':
    exp1 = make_sum('x', '3')
    exp2 = make_product('x', 'y')
    exp3 = make_product(exp2, exp1)
    exp4 = make_exponentiation('x', '3')
    exp5 = make_sum('1', '0', 'y', '4', 'x')
    exp6 = make_product('1', '0', '-3', '4', 'x')

    display(exp1)
    display(exp2)
    display(exp3)
    display(exp4)
    display(exp5)
    display(exp6)
    display(deriv(exp1, 'x'))
    display(deriv(exp2, 'x'))
    display(deriv(exp3, 'x'))
    display(deriv(exp4, 'x'))
    display(make_sum(exp1, exp2, exp4))
    display(deriv(exp3, 'x'))
    display(deriv(make_product('x', 'y', exp1), 'x'))
    display(deriv(exp5, 'x'))

