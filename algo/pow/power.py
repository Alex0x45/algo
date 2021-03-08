"""Integer powers"""


def recpow(b, n):

    def accpow(b, n, acc):
        
        if n == 0:
            return acc
        elif n % 2 == 0:
            return accpow(b * b, n // 2, acc)
        else:
            return accpow(b * b, (n - 1) // 2, acc * b)

    return accpow(b, n, 1)


def pow(b, n):

    acc = 1
    while n > 0:
        if n % 2 == 1:
            acc *= b

        n //= 2
        b = b * b
    
    return acc
