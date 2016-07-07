from math import sqrt


#--------------------------------有理数算术（练习 2.1)----------------------------------

def make_rat(n, d):
    def gcd(a, b):
        if b == 0: return a
        else: return gcd(b, a%b)
    if d < 0:    # 练习2.1
        n = -n
        d = -d
    g = gcd(n, d)
    return (n//g, d//g)    # py3.0 '/'为真除法，会出现小数

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rat(x, y):
    return make_rat(numer(x)*denom(y)+numer(y)*denom(x), denom(x)*denom(y))

def sub_rat(x, y):
    return make_rat(numer(x)*denom(y)-numer(y)*denom(x), denom(x)*denom(y))

def mul_rat(x, y):
    return make_rat(numer(x)*numer(y), denom(x)*denom(y))

def div_rat(x, y):
    return make_rat(numer(x)*denom(y), denom(x)*numer(y))

def equal_rat(x, y):
    if numer(x)*denom(y) == denom(x)*numer(y): return True
    else: return  False

def print_rat(x):
    return print('{0}/{1}'.format(numer(x), denom(x)))


#------------------------------抽象屏障（练习 2.2&2.3）---------------------------------

def make_point(x, y):
    return (x, y)

def x_point(p):
    return p[0]

def y_point(p):
    return p[1]

def print_point(p):
    return print('({0}, {1})'.format(x_point(p), y_point(p)))

def make_segment(p1, p2):
    return (p1, p2)

def start_segment(s):
    return s[0]

def end_segment(s):
    return s[1]

def midpoint_segment(s):
    xs = x_point(start_segment(s))
    ys = y_point(start_segment(s))
    xe = x_point(end_segment(s))
    ye = y_point(end_segment(s))
    return make_point((xs+xe)/2, (ys+ye)/2)

def length_of_segment(s):
    xs = x_point(start_segment(s))
    ys = y_point(start_segment(s))
    xe = x_point(end_segment(s))
    ye = y_point(end_segment(s))
    if xs*xe < 0: x = xs+xe
    else: x = xs-xe
    if ys*ye < 0: y = ys+ye
    else: y = ys-ye
    return round(sqrt(x**2+y**2))

def print_segment(s):
    return print('{0}--{1}'.format(start_segment(s), end_segment(s)))

def make_rectangle_by_point(pa, pb, pc, pd):
    S1 = make_segment(pa, pb)
    S2 = make_segment(pb, pc)
    S3 = make_segment(pc, pd)
    S4 = make_segment(pd, pa)
    return (S1, S2, S3, S4)

def make_rectangle_by_segment(l, w):
    if start_segment(l) == start_segment(w):    # 找公共点B，线S1有点p1,q1，线S2有点p2,q2
        pb = start_segment(l)
        pa = end_segment(l)
        pc = end_segment(w)
    elif start_segment(l) == end_segment(w):
        pb = start_segment(l)
        pa = end_segment(l)
        pc = start_segment(w)
    else:
        pb = end_segment(l)
        pa = start_segment(l)
        if pb == start_segment(w): pc = end_segment(w)
        else: pc = start_segment(w)
    pd = make_point(x_point(pa)+x_point(pc)-x_point(pb), \
                    y_point(pa)+y_point(pc)-y_point(pb))    # 向量运算：OD=OA+AD AD=BC
    S1 = make_segment(pa, pb)
    S2 = make_segment(pb, pc)
    S3 = make_segment(pc, pd)
    S4 = make_segment(pd, pa)
    return (S1, S2, S3, S4)
    
def s1_segment(r):
    return r[0]

def s2_segment(r):
    return r[1]

def s3_segment(r):
    return r[2]

def s4_segment(r):
    return r[3]

def length_of_rectangle(r):
    S1 = s1_segment(r)
    return length_of_segment(S1)

def width_of_rectangle(r):
    S2 = s2_segment(r)
    return length_of_segment(S2)

def perimeter_rectangle(r):
    length = length_of_rectangle(r)
    width = width_of_rectangle(r)
    return (length+width)*2

def area_rectangle(r):
    length = length_of_rectangle(r)
    width = width_of_rectangle(r)
    return length*width

def print_rectangle(r):
    print('rectangle')
    print_segment(s1_segment(r))
    print_segment(s2_segment(r))
    print_segment(s3_segment(r))
    print_segment(s4_segment(r))


#-------------------------------数据（练习 2.4-2.6）----------------------------------

def cons_ab(a, b):
    return (2**a)*(3**b)

def car_ab(z):
    if z%2 == 0:
        return 1+car_ab(z/2)
    else: return 0

def cdr_ab(z):
    if z%3 == 0:
        return 1+cdr_ab(z/3)
    else: return 0

def add_1(n):
    return lambda f: lambda x: f(n(f)(x))    # 将被加数调用一次lambda f和lambda x嵌套进lambda f

def zero():
    return lambda f: lambda x: x

def one():
    return lambda f: lambda x: f(x)

def two():
    return lambda f: lambda x: f(f(x))

def add_method(a, b):
    return lambda f: lambda x: a(f(b(f)(x)))

#------------------------------区间算术（练习 2.7-2.16）--------------------------------

def make_interval(a, b):
    lo = min(a, b)
    up = max(a, b)
    return (lo, up)

def lower_bound(z):
    return z[0]

def upper_bound(z):
    return z[1]

def add_interval(x, y):
    lower = lower_bound(x)+lower_bound(y)
    upper = upper_bound(x)+upper_bound(y)
    return make_interval(lower, upper)

def sub_interval(x, y):
    lower = lower_bound(x)-upper_bound(y)
    upper = upper_bound(x)-lower_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    p1 = lower_bound(x)*lower_bound(y)
    p2 = lower_bound(x)*upper_bound(y)
    p3 = upper_bound(x)*lower_bound(y)
    p4 = upper_bound(x)*upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    if lower_bound(y)*upper_bound(y) <= 0 :
        return 'Error interval, interval can\'t span zero'
    reciprocal_y = make_interval(1/lower_bound(y), 1/upper_bound(y))
    return mul_interval(x, reciprocal_y)

def new_mul_interval(x, y):
    def endpoint_sign(k):
        if upper_bound(k) >= 0 and lower_bound(k) >= 0: return 1
        elif upper_bound(k) < 0 and lower_bound(k) < 0: return -1
        else: return 0
    x_lo = lower_bound(x)
    x_up = upper_bound(x)
    y_lo = lower_bound(y)
    y_up = upper_bound(y)
    sign = endpoint_sign
    if sign(x) > 0:
        if sign(y) > 0: return make_interval(x_lo*y_lo, x_up*y_up)
        elif sign(y) < 0: return make_interval(x_up*y_lo, x_lo*y_up)
        else: return make_interval(x_up*y_lo, x_up*y_up)
    elif sign(x) < 0:
        if sign(y) > 0: return make_interval(x_lo*y_up, x_up*y_lo)
        elif sign(y) < 0: return make_interval(x_up*y_up, x_lo*y_lo)
        else: return make_interval(x_lo*y_up, x_lo*y_lo)
    else:
        if sign(y) > 0: return make_interval(x_lo*y_up, x_up*y_up)
        elif sign(y) < 0: return make_interval(x_up*y_lo, x_lo*y_lo)
        else: return make_interval(min(x_lo*y_up, x_up*y_lo), \
                                   max(x_lo*y_lo, x_up*y_up))

def make_center_width(c, w):
    return make_interval(c-w, c+w)

def center(r):
    return (lower_bound(r)+upper_bound(r))/2

def width(r):
    return (upper_bound(r)-lower_bound(r))/2

def make_center_percent(c, p):
    w = c*p
    return make_center_width(c, w)

def percent(r):
    c = center(r)
    w = width(r)
    return w/c



if __name__ == '__main__':
    m = make_rat
    n = numer
    d = denom
    addr = add_rat
    subr = sub_rat
    mulr = mul_rat
    divr = div_rat
    eqr = equal_rat
    printr = print_rat

    x = m(1,2)
    y = m(1,-3)
    printr(addr(x, y))
    printr(subr(x, y))
    printr(mulr(x, y))
    printr(divr(x, y))
    print(eqr(x, y))

    p1 = make_point(1, 3)
    p2 = make_point(4, 3)
    s = make_segment(p1,p2)
    print_point(start_segment(s))
    print_point(end_segment(s))
    print_point(midpoint_segment(s))

    pa = make_point(1, 2)
    pb = make_point(4, 2)
    pc = make_point(4, 4)
    pd = make_point(1, 4)
    l = make_segment(pc, pd)
    w = make_segment(pd, pa)
    r1 = make_rectangle_by_point(pa, pb, pc, pd)
    r2 = make_rectangle_by_segment(l, w)
    print_rectangle(r1)
    print_rectangle(r2)
    print('length of rectangle:    r1:{0}  r2:{1}'.format
          (length_of_rectangle(r1), length_of_rectangle(r2)))
    print('width of rectangle:     r1:{0}  r2:{1}'.format
          (width_of_rectangle(r1), width_of_rectangle(r2)))
    print('perimeter of rectangle: r1:{0}  r2:{1}'.format
          (perimeter_rectangle(r1), perimeter_rectangle(r2)))
    print('area of rectangle:      r1:{0}  r2:{1}'.format
          (area_rectangle(r1), area_rectangle(r2)))

    a = 3
    b = 2
    z = cons_ab(a, b)
    print('couns(a,b)=', z)
    print('a =', car_ab(z))
    print('b =', cdr_ab(z))

    def mul_interval_test(a, b, c, d):
        x = make_interval(a, b)
        y = make_interval(c, d)
##        print(mul_interval(x, y))
##        print(new_mul_interval(x, y))
        if mul_interval(x, y) == new_mul_interval(x, y):
            return True
        else: return False

    def multest(a, b, c, d):
        L = [a, b, c, d]
        for k in range(0,2):
            for i in range(0, 4):
                L[i] = -L[i]
                print(L)
                print(mul_interval_test(L[0], L[1], L[2], L[3]))
        L[0] = -L[0]
        L[2] = -L[2]
        print(L)
        print(mul_interval_test(L[0], L[1], L[2], L[3]))

##    multest(2, 4, 3, 5)
##    multest(0, 4, 3, 5)
##    multest(0, 0, 3, 5)
##    multest(2, 0, 3, 5)

    A = make_interval(2, 2.00001)
    B = make_interval(2, 2.00001)
    print(div_interval(A, A),div_interval(A, B))
