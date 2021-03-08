"""Integer powers"""


def recpow(b, n):

    if n == 0:
        return 1
    elif n % 2 == 0:
        return recpow(b * b, n // 2)
    else:
        return recpow(b * b, (n - 1) // 2) * b


def pow(b, n):

    def accpow(b, n, acc):
        
        if n == 0:
            return acc
        elif n % 2 == 0:
            return accpow(b * b, n // 2, acc)
        else:
            return accpow(b * b, (n - 1) // 2, acc * b)

    if n == 0:
        return 1
    else:
        return accpow(b, n, 1)
