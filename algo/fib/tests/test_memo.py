#!/usr/bin/env python

"""Tests for `memofib` function."""

from fixture import list_10


from fib import gen


def test_negative1():
    assert 0 == gen.memofib(-1)


def test_0_to_10(list_10):
    for n in range(11):
        assert list_10[n] == gen.memofib(n)
