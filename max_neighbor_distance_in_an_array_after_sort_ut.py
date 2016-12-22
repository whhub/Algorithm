"""
#coding=utf8
无序数组排序后的最大相邻差值 unit test
"""

from nose.tools import *
from max_neighbor_distance_in_an_array_after_sort import calculate


def test_max_neighbor_distance_in_an_array_after_sort():
    # Arrange
    num_list = [2, 6, 3, 4, 5, 10, 9]
    # Act

    actual = calculate(num_list)
    # Assert
    assert_equal(3, actual)


