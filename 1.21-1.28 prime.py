from Timer import timer
from random import randrange


@timer
def prime(n, test=2):
    if test == 2:
        if test**2 > n:
            return n
        elif n % test == 0:
            return test
        else:
            return prime(n, test+1)
    else:
        if test**2 > n:
            return n
        elif n % test == 0:
            return test
        else:
            return prime(n, test+2)


def expmod(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (expmod(n/2, a)**2) % n
    else:
        return (a*expmod(n-1, a)) % n


@timer
def fermat_prime(n, times=10):
    a = randrange(1, n)
    if times == 0:
        return n
    elif expmod(a, n) == a:
        return fermat_prime(n, times-1)
    else:
        return False


def search_odd_prime(n, count=3):
    def counter(n, count):
        if count>0:
            if fermat_prime(n) == n:
                print('{0}***{1}'.format(n, fermat_prime.allTime))
                counter(n+2, count-1)
            else:
                counter(n+2, count)
    if n % 2 == 0:
        n += 1
    return counter(n, count)

if __name__ == '__main__':
    test = search_odd_prime
    
##    test(10000)
##    test(100000)
##    test(1000000)
