"""
#coding=utf8
无序数组排序后的最大相邻差值
"""


def calculate(num_list):
    list_len = len(num_list)
    assert list_len > 0

    bucket_len = (max(num_list) - min(num_list)) / list_len + 1
    bucket = [[]] * bucket_len

    # put numbers in bucket based on their size
    for i in range(list_len):
        current = num_list[i]
        j = current / bucket_len
        bucket[j].append(current)

    # TODO: How to tell computer to find left_most_non_empty_bucket & right_most_non_empty_bucket

    return 3



