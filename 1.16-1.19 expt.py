def expt(b, n, p=1):
    if n == 0: return p
    else: return expt(b, n-1, b*p)

def fast_expt(b, n, p=1):
    if n == 0: return p
    elif n%2 == 0: return fast_expt(b**2, n/2, p)
    else: return fast_expt(b, n-1, b*p)

def mul(a,b):
    if b == 1: return a
    elif b%2 == 0: return mul(a+a, b/2)
    else: return a + mul(a, b-1)
