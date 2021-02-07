"""Integer powers"""


def recpow(b, n):

    def pow_acc(b, n, acc):
        if n == 1:
            return acc
        elif n % 2 == 0:
            return pow_acc(b, n // 2, acc * acc)
        else:
            return pow_acc(b, n // 2, acc * acc * b)

    if n == 0:
        return 1
    else:
        return pow_acc(b, n, b)


def pow(b, n):
    if n == 0:
        return 1
    
    acc = b
    while n > 1:
        if n % 2 == 0:
            acc = acc * acc
        else:
            acc = acc * acc * b

        n = n // 2

    return acc
