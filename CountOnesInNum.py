"""
This program used to count ones in a binary num
"""


def count_ones_in_num(num):
    count = 0
    while num:
        count += 1
        num &= num - 1
    return count

import sys

print("This program used to count ones in a binary num, input a number >> ")

number = int(input())

print("Output %d" % count_ones_in_num(number))



