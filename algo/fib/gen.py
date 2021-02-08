"""Generators."""


from functools import lru_cache


def fibgen(n):
    yield 0
    if n > 0:
        yield 1
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield b


def fib(n):
    gen = fibgen(n)
    for _ in range(n):
        next(gen)
    return next(gen)


@lru_cache(maxsize=None)
def memofib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memofib(n - 1) + memofib(n - 2)


def fastfib(n):

    def f2n_and_f2n1(n):
        
        def fn_to_f2n(fn, fn1):
            f2n = fn * (2 * fn1 - fn)
            f2n1 = fn1 * fn1 + fn * fn
            return (f2n, f2n1)
            
        if n == 0:
            return (0, 1)
        elif n == 1:
            return (1, 2)
        else:   
            k = n // 2 
            (f2k, f2k1) = f2n_and_f2n1(k)
            (fn, fn1) = (f2k, f2k1) if n %2 == 0 else (f2k1, f2k + f2k1)
            (f2n, f2n1) = fn_to_f2n(fn, fn1)
            return (f2n, f2n1)

    if n <= 0:
        return 0

    l = n // 2
    (f2l, f2l1) = f2n_and_f2n1(l)
    return f2l if n % 2 == 0 else f2l1
