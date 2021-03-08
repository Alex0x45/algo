from pow import power


def test_2_pow_0():
    assert 1 == power.recpow(2, 0)


def test_2_pow_1():
    assert 2 == power.recpow(2, 1)


def test_2_pow_2():
    assert 4 == power.recpow(2, 2)


def test_2_pow_6():
    assert 64 == power.recpow(2, 6)


def test_2_pow_10():
    assert 1024 == power.recpow(2, 10)


def test_1_pow_0():
    assert 1 == power.recpow(1, 0)


def test_1_pow_1():
    assert 1 == power.recpow(1, 1)


def test_1_pow_2():
    assert 1 == power.recpow(1, 1)


def test_1_pow_10():
    assert 1 == power.recpow(1, 2)


def test_pow_equal_builtin():
    for b in range(1, 4):
        for n in range(10):
            assert power.recpow(b, n) == b**n
