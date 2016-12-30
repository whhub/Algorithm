# coding=utf8
"""
选择排序的工作原理如下。首先在未排序序列中找到最小元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小
元素，放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。选择排序的主要优点与数据移动有关。如果某个元素位于正确的最
终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总
共进行至多n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。如果移动元素的代价非常大，使
用选择排序可以保证最少次数的数据移动。
"""


def selection_sort(a):
    # compare_count = 0
    # swap_count = 0
    n = int(len(a))
    for i in range(n-1):
        min_num = a[i]
        min_index = i
        for j in range(i+1, n):
            # compare_count += 1
            if min_num > a[j]:
                min_index = j
                min_num = a[j]
        if min_index != i:
            # swap_count += 1
            a[min_index], a[i] = a[i], a[min_index]
    # print("Compared:%d, Swapped:%d" % (compare_count, swap_count))
    return a

from RandomList import random_list

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
selection_sort(rand_nums)
print("After  sort: ", len(rand_nums), rand_nums)
