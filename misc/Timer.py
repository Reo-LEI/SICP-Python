import time

def TIMER(Trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
        def __call__(self, *args):
            start = time.clock()
            result = self.func(*args)
            elapsed = time.clock()-start
            if Trace:
                print('Time:{0} *** {1}'.format(self.func.__name__, elapsed))
            return result
    return Timer

class Timer:
    def __init__(self, func):
        self.func = func
##        print('class:'+str(id(Timer)))
##        print('instance:'+str(id(self)))
    def __call__(self, *args):
        start = time.clock()
        result = self.func(*args)
        elapsed = time.clock()-start
        print('Time:{0} *** {1}'.format(self.func.__name__, elapsed))
        return result

def timer(func):
    def onCall(*args):
        start = time.clock()
        result = func(*args)
        elapsed = time.clock()-start
        onCall.allTime += elapsed
##        print('Time:{0} *** {1}'.format(func.__name__, elapsed))
        return result
    onCall.allTime = 0
##    print('timer:'+str(id(timer)))
##    print('onCall:'+str(id(onCall)))
    return onCall



if __name__=='__main__':
    
    ##@timer(Trace=True)
    @timer
    def smallest_divisor(n,test=2):
        if test**2 > n: return n
        elif n%test == 0: return test
        else: return smallest_divisor(n, test+1)

    ##@timer(Trace=True)
    @timer
    def test(n):
        print(n)
        
