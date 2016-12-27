from nose.tools import *
from sqrt import sqrt


def test_sqrt_negative_number_return_0():
    assert_equal(0, sqrt(-1, 0.21))


def test_sqrt_zero_precision_return_0():
    assert_equal(0, sqrt(3, 0))


def test_sqrt():
    assert_equal(3, sqrt(10, 1))

