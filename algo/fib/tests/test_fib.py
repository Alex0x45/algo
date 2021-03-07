#!/usr/bin/env python

"""Tests for `fib` function."""

from fib import gen


def test_negative1():
    assert 0 == gen.fib(-1)


def test_list(list_fib):
    for (n, val) in enumerate(list_fib):
        assert val == gen.fib(n)
