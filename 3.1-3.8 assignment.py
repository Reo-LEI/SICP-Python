from symbolic import *
import random
import sys

sys.setrecursionlimit(1000000000)


# 3.1.1
def withdraw():
    balance = 100

    def counter(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return 'Insufficient funds'
    return counter


def make_withdraw(balance):
    def counter(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return 'Insufficient funds'
    return counter


def make_account(balance):
    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return 'Insufficient funds'

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def dispatch(m):
        if eq('withdraw', m):
            return withdraw
        elif eq('deposit', m):
            return deposit
        else:
            return 'error: Unknown request -- MAKE-ACCOUNT'
    return dispatch


# exer 3.1
def make_accumulator(init):
    def counter(value):
        nonlocal init
        init = init + value
        return init
    return counter


# exer 3.2
def make_monitored(func):
    counter = 0

    def mf(value):
        nonlocal counter
        if eq('how_many_calls?', value):
            return counter
        elif eq('reset_count', value):
            counter = 0
        else:
            counter += 1
            return func(value)
    return mf


# exer 3.3
def new_make_account(balance, set_password):
    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return 'Insufficient funds'

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def dispatch(password, m):
        if eq(password, set_password):
            if eq('withdraw', m):
                return withdraw
            elif eq('deposit', m):
                return deposit
            else:
                return 'error: Unknown request -- MAKE-ACCOUNT'
        else:
            return 'Incorrect password'
    return dispatch


# exer 3.4
def new_make_account_(balance, set_password):
    record = 0

    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return 'Insufficient funds'

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def call_the_cops():
        return 'The cops are on there way'

    def dispatch(password, m):
        if eq(password, set_password):
            if eq('withdraw', m):
                return withdraw
            elif eq('deposit', m):
                return deposit
            else:
                return 'error: Unknown request -- MAKE-ACCOUNT'
        else:
            nonlocal record
            record += 1
            if record > 7:
                return call_the_cops()
            else:
                return 'Incorrect password'
    return dispatch


# 3.1.2
def estimate_pi(trials):
    return (6 / monte_carlo(trials, cesaro_test()))**0.5


def cesaro_test():
    def gcd(v1, v2):
        if not v2:
            return v1
        else:
            return gcd(v2, v1 % v2)
    if gcd(random.randint(1, 1000000), random.randint(1, 1000000)) == 1:
        return True
    else:
        return False


def monte_carlo(trials, experiment):
    def iter(trials_remaining, trials_passed):
        if not trials_remaining:
            return trials_passed/trials
        elif experiment:
            return iter(trials_remaining-1, trials_passed+1)
        else:
            return iter(trials_remaining-1, trials_passed)
    return iter(trials, 0)


# exer 3.5
def estimate_integral(p, x1, x2, y1, y2, trials):
    return 4*monte_carlo(trials,
                         lambda: p(random_in_range(x1, x2),
                                   random_in_range(y1, y2)))


def get_pi(trials):
    return estimate_integral(lambda x, y: True if x**2+y**2 < 1 else False,
                             -1.0, 1.0, -1.0, 1.0, trials)


def random_in_range(low, high):
    range = high - low
    return low + random.randrange(0, range)


# exer 3.6
def rand(symbol):
    x = 0

    def update(x):
        # nonlocal x
        # x = rand_update(x)
        return x

    def reset(v):
        nonlocal x
        x = v

    if eq(symbol, 'generate'):
        return update
    elif eq(symbol, 'reset'):
        return reset
    else:
        'error'


# exer 3.7
def make_join(account, origin_password, set_password):
    return lambda password, mode: (account(origin_password, mode)
                                   if eq(set_password, password)
                                   else "Incorrect another password")


# exer 3.8
def func():
    counter = 0

    def first(first_value):
        nonlocal counter
        if not counter:
            counter += 1
            return first_value
        else:
            return 0
    return first

if __name__ == '__main__':
    # 3.1.1
    print(withdraw()(25))
    print(withdraw()(25))
    x = withdraw()
    print(x(25))
    print(x(25))
    print(x(60))

    w1 = make_withdraw(100)
    w2 = make_withdraw(100)
    print(w1(50), w2(70), w2(40), w1(40))

    acc = make_account(100)
    acc2 = make_account(100)
    acc_w = acc('withdraw')
    acc_d = acc('deposit')
    print(acc_w(50), acc_w(60), acc_d(40), acc_d(60))
    print(acc2('withdraw')(10))

    # exer 3.1
    A = make_accumulator(5)
    B = make_accumulator(10)
    print(A(10), A(10))
    print(B(2), B(-1))

    # exer 3.2
    s = make_monitored(lambda x: x**0.5)
    print(s(100), s('how_many_calls?'))
    s('reset_count')
    print(s('how_many_calls?'))

    # exer 3.3
    acc = new_make_account(100, 'secret-password')
    print(acc('secret-password', 'withdraw')(40))
    print(acc('secret-password', 'deposit')(50))
    print(acc('wrong-password', 'deposit'), acc('wrong-password', 'deposit'))

    # exer 3.4
    a = new_make_account_(100, 'secret-password')
    print([a('wrong-password', 'deposit') for i in range(0, 8)])

    # 3.1.2
    print(estimate_pi(10000))

    # exer 3.5
    print(get_pi(5))

    # exer 3.8
    f = func()
    print(f(1)+f(0))
    print(f(0)+f(1))
