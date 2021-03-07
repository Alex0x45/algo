"""Integer powers"""


def pow(b, n):

    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(b * b, n // 2)
    else:
        return pow(b * b, (n - 1) // 2) * b
