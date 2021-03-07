#!/usr/bin/env python

"""Tests for `fibgen` function."""

from fib import gen


def make_list(n):
    return [i for i in gen.fibgen(n)]


def test_negative1():
    assert [0] == make_list(-1)


def test_0():
    assert [0] == make_list(0)


def test_1():
    assert [0, 1] == make_list(1)


def test_list(list_fib):
    for i in range(len(list_fib)):
        expected = list_fib[:(i + 1)]
        actual = make_list(i)
        assert expected == actual
