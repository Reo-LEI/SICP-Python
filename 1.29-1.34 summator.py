def summator(func, k, _next, n):
    if k > n: return 0
    else: return func(k)+summator(func, _next(k), _next, n)

def sum_iter(func, k, _next, n, result=0):
    if k > n: return result
    else: return sum_iter(func, _next(k), _next, n, func(k)+result)

def simpson(f, a, b, n):
    def factor(k):
        if k == 0 or k == n: return 1
        elif k%2 == 0: return 2
        else: return 4
    def func(k): return factor(k)*f(a+k*h)
    def _next(k): return k+1
    h=(b-a)/n
    if n%2 == 0: return sum_iter(func, 0, _next, n)*h/3
    else: return print('n can\'t be odd')

def cube(x): return x**3

def product(func, k, _next, n):
    if k > n: return 1
    else: return func(k)*product(func, _next(k), _next, n)

def product_iter(func, k, _next, n, result=1):
    if k > n: return result
    else: return product_iter(func, _next(k), _next, n, func(k)*result)

def quarter_pi(n):
    def func(k):
        if k%2 == 0: return (k+2)/(k+3)
        else: return (k+3)/(k+2)
    def _next(k): return k+1
    return product(func, 0, _next, n)*4

def accumulate(combiner, null_value, term, k, _next, n):
    if k > n: return null_value
    else:
        if combiner == 'addition':
            return term(k)+accumulate(combiner, null_value, term, _next(k), _next, n)
        if combiner == 'multiplication':
            return term(k)*accumulate(combiner, null_value, term, _next(k), _next, n)
      
def accumulate_iter(combiner, null_value, term, k, _next, n, restult=0):
    if k > n: return null_value
    else:
        if combiner == 'addition':
            return accumulate_iter(combiner, null_value, term, _next(k), _next, n, term(k)+result)
        if combiner == 'multiplication':
            return accumulate_iter(combiner, null_value, term, _next(k), _next, n, term(k)*result)

def simpson_accumulate(f, a, b, n):
    def factor(k):
        if k == 0 or k == n: return 1
        elif k%2 == 0: return 2
        else: return 4
    def func(k): return factor(k)*f(a+k*h)
    def _next(k): return k+1
    h=(b-a)/n
    if n%2 == 0: return accumulate('addition', 0, func, 0, _next, n)*h/3
    else: return print('n can\'t be odd')

def filtered_accumulate(filter_func, combiner, null_value, term, k, _next, n):
    if k > n: return null_value
    else:
        if filter_func(k):
##            print(k)
            if combiner == 'addition':
                return term(k)+filtered_accumulate(filter_func, combiner,
                                                   null_value, term, _next(k), _next, n)
            if combiner == 'multiplication':
                return term(k)*filtered_accumulate(filter_func, combiner,
                                                   null_value, term, _next(k), _next, n)
        else: return filtered_accumulate(filter_func, combiner,
                                         null_value, term, _next(k), _next, n)

def filtered_accumulate_iter(filter_func, combiner, null_value, term, k, _next, n, result=0):
    if k > n: return null_value
    else:
        if filter_func(k):
##            print(k)
            if combiner == 'addition':
                return filtered_accumulate(filter_func, combiner, null_value,
                                           term, _next(k), _next, n, term(k)+result)
            if combiner == 'multiplication':
                return filtered_accumulate(filter_func, combiner, null_value,
                                           term, _next(k), _next, n, term(k)*result)
        else: return filtered_accumulate(filter_func, combiner, null_value,
                                           term, _next(k), _next, n, result)
def prime(n,test=2):
    if test == 2:
        if test**2 > n: return True
        elif n%test == 0: return False
        else: return prime(n, test+1)
    else:
        if test**2 > n: return True
        elif n%test == 0: return False
        else: return prime(n, test+2)

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)


def prime_accumulate(a, b):
    def replace(x): return x
    def _next(k): return k+1
    return filtered_accumulate(prime, 'addition', 0, replace, a, _next, b)

def gcd_accumulate(n):
    def replace(x): return x
    def _next(k): return k+1
    def gcd_filter(i):
        if gcd(i, n) == 1: return True
        else: return False
    return filtered_accumulate(gcd_filter, 'multiplication', 1, replace, 1, _next, n)
    

if __name__=='__main__':
    test1 = simpson
    print(test1(cube, 0, 1, 100))
    print(test1(cube, 0, 1, 500))
    test2 = quarter_pi
    print(test2(900))
    test3 = simpson_accumulate
    print(test3(cube, 0, 1, 100))
    test4 = prime_accumulate
    print(test4(1, 10))
    test5 = gcd_accumulate
    print(test5(10))
