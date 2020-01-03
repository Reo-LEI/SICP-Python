def cons(a, b):
    return (a, b)

def car(x):
    return x[0]

def cdr(x):
    return x[1]

def lister(*args):
    def coner(x, y):
        if y == []:
            return cons(x, None)
        else:
            return cons(x, coner(y[0], y[1:]))
    L = list(args)
    first, other = L[0], L[1:]
    return coner(first, other)

def list_ref(item, n):
    if n == 0: return car(item)
    else: return list_ref(cdr(item), n-1)

def length(item):
    if item == None: return 0
    else: return 1+length(cdr(item))

def append(list1, list2):
    if list1 == None: return list2
    else: return cons(car(list1), append(cdr(list1), list2))

def last_pair(item):
    if cdr(item) == None: return car(item)
    else: return last_pair(cdr(item))

def reverse(item):
    if item == None: None
    else: return cons(reverse(cdr(item)), car(item))

def mapper(func, item):
    if item == None: return None
    else: return cons(func(car(item)), mapper(func, cdr(item)))

def for_each(proc, item):
    if item == None: pass
    else:
        proc(car(item))
        for_each(proc, cdr(item))

def cc(amount, coin_values):
    def no_more(c):
        if c == None: return True
        else: return False
    def except_first_denomination(c):
        return cdr(c)
    def first_denomination(c):
        return car(c)
    if amount == 0: return 1
    elif amount < 0 or no_more(coin_values): return 0
    else:
        return cc(amount, except_first_denomination(coin_values)) + \
               cc(amount-first_denomination(coin_values), coin_values)

def same_parity(*args):
    def coner(x, y, p):
        if x%2 == p:
            if y == []:
                return cons(x, None)
            else:
                return cons(x, coner(y[0], y[1:], p))
        else:
            if y == []:
                return None
            else:
                return coner(y[0], y[1:], p)
    L = list(args)
    first, other = L[0], L[1:]
    if first%2 == 0: parity = 0
    else: parity = 1
    return coner(first, other, parity)

def scale_list(item, factor):
    return mapper(lambda x: x*factor, item)

def square_list(item):
    return mapper(lambda x: x**2, item)

def square_list_recursion(item):
    if item == None: return None
    else: return cons(car(item)**2, square_list_recursion(cdr(item)))

def square_list_iter(item, result=None):
    if item == None: return result
    else: return square_list_iter(cdr(item), cons(car(item)**2, result))


if __name__ == '__main__':
    testlist1 = lister(1, 2, 3, 4, 5, 6)
    testlist2 = lister(4, 5, 7, 3, 5, 1)
    print(testlist1)
    print(testlist2)
    print(list_ref(testlist1, 4))
    print(length(testlist1))
    print(append(testlist1, testlist2))
    print(last_pair(testlist2))
    print(reverse(testlist1))
    us_coins = lister(50, 25, 10, 5, 1)
    uk_coins = lister(100, 50, 20, 10, 5, 2, 1, 0.5)
    print(cc(100, us_coins))
    print(same_parity(3, 5, 2, 7, 8, 0))
    print(scale_list(testlist1, 2))
    print(square_list_recursion(testlist1))
    print(square_list(testlist1))
    print(square_list_iter(testlist1))
    for_each(print, testlist1)
