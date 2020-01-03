from math import log

def fixed_point(func, guess, tolerance=0.0000001):
    #若x满足f(x)=x，则x为f(x)的不动点，可通过反复调用f(guess）逼近x
    '''print(func(guess))'''    #测试用输出
    if abs(func(guess)-guess) < tolerance: return guess
    else: return fixed_point(func, func(guess), tolerance)

def cont_frac(funcN, funcD, n, k=1):
    #无穷连分式（递归计算过程）
    if k == n: return funcN(k)/funcD(k)
    else: return funcN(k)/(funcD(k)+cont_frac(funcN, funcD, n, k+1))

def cont_frac_iter(funcN, funcD, n, result=0):
    #无穷连分式（迭代计算过程）
    if n == 0: return result
    else: return cont_frac_iter(funcN, funcD, n-1, funcN(n)/(funcD(n)+result))    

def tan_cf(x,k):
    #正切函数连分式表示
    return cont_frac_iter(lambda i: x if i == 1 else -x**2, lambda i: i*2-1, k)

def average_damp(g):
    #平均阻尼变换
    return lambda x: (x+g(x))/2

def sqrt_fixed_point(x):
    #不动点法求解平方根：假设y**2=x，y=x/y,不动点y为x的平方根
    return fixed_point(average_damp(lambda y: x/y), 1.0)

def deriv(g, dx=0.00001):
    #g(x)求导，返回g'(x)
    return lambda x: (g(x+dx)-g(x))/dx

def newton_transform(g):
    #牛顿变换，g(x)=0的解x等于g(x)牛顿变换后f(x)的一个不动点
    return lambda x: x-(g(x)/deriv(g)(x))

def newton_method(g, guess):
    #牛顿法，求g(x)=0的解x
    return fixed_point(newton_transform(g), guess)

def sqrt_newton_method(x):
    #牛顿法求解平方根：假设y**2=x，g(y)=y**2-x=0,不动点y为x的平方根
    return newton_method(lambda y: y**2-x, 1.0)

def fixed_point_of_transform(transform, g, guess):
    #不动点变换
    return fixed_point(transform(g), guess)

def cubic(a, b, c):
    #练习1.40
    return newton_method(lambda x: x**3+a*x**2+b*x+c, 1.0)

def inc(x): return x+1    #练习1.41(a)

def double(func): return lambda x: func(func(x))    #练习1.41(b)

def compose(f, g): return lambda x:f(g(x)) #练习1.42

def repeated(func, n):
    #练习1.43 recursion
    if n == 1: return  func
    else: return compose(func, repeated(func, n-1))

def repeated_iter(func, n, result=lambda x: x):
    #练习1.43 iteration
    if n == 0: return result
    else: return repeated_iter(func, n-1, compose(func, result))

def smooth(f, dx=0.00001):
    #练习1.44(a)
    return lambda x: (f(x+dx)+f(x)+f(x-dx))/3

def smooth_n_time(f, n):
    #练习1.44(b)
    return repeated(smooth, n)(f)

def lg(n):
    #练习1.45(a)
    if n/2 > 1: return lg(n/2)+1
    elif n/2 < 1: return 0
    else: return 1

def nth_root(x,n):
    #练习1.45(b)
    return fixed_point(repeated(average_damp, lg(n))(lambda y: x/y**(n-1)), 1.0)

def iter_improve(test, improve, guess, tolerance=0.0000001):
    #练习1.46(a)
    if test(guess) < tolerance: return guess
    else: return iter_improve(test, improve, improve(guess), tolerance)
    
def re_fixed_point(func, guess):
    #练习1.46(b)
    return iter_improve(lambda x: abs(func(x)-x), func, guess)

def re_sqrt(x):
    #练习1.46(c)
    def func(a): return average_damp(lambda y: a/y)
    return iter_improve(lambda guess: abs(func(x)(guess)-guess), func(x), 1.0)

if __name__=='__main__':
    test = fixed_point
    print(sqrt_fixed_point(2), '\n')
    print(test(lambda x: 1+1/x, 1.5), '\n')
    print(test(lambda x: log(1000)/log(x), 2), '\n')
    print(test(lambda x: (x+log(1000)/log(x))/2, 2), '\n')
    print(1/cont_frac_iter(lambda i: 1.0, lambda i: 1.0, 100), '\n')
    print(list(map(lambda i: (i+1)//3*2 if (i+1)%3 == 0 else 1, range(1,20))), '\n')
    print(cont_frac_iter(lambda i: 1.0,
                         lambda i: (i+1)/3*2 if (i+1)%3 == 0 else 1, 100)+2,'\n')
    print(tan_cf(10,100),'\n')
    print(sqrt_newton_method(2),'\n')
    print(cubic(3, 2, 1),'\n')
    print(double(double(double))(inc)(5),'\n')
    print(compose(lambda x: x**2, inc)(6),'\n')
    print(repeated_iter(lambda x: x**2, 2)(5),'\n')
    print(smooth(lambda x: x**2)(5),'\n')
    print(repeated(smooth, 10)(lambda x: x**2)(5),'\n')
    print(smooth_n_time(lambda x: x**2, 10)(5),'\n')
    print(nth_root(100,100),'\n')
    print(re_fixed_point(lambda x: 1+1/x, 1.5), '\n')
    print(re_sqrt(2), '\n')
