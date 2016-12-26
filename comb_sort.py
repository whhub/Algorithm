"""
#coding=utf8
梳子排序是改良自冒泡排序和快速排序的不稳定排序算法，其要旨在于消除乌龟（在阵列尾部的小数值，这些数值是造成泡沫排序缓慢的
主因；相对地，兔子指的是在阵列前端的大数值，它不影响冒泡排序的性能）。在冒泡排序中，只比较阵列中相邻的二项，即比较的二项
的间距是1，梳子排序提出此间距其实可大于1，改自插入排序的希尔排序同样提出相同观点。梳子排序中，开始时的间距设定为阵列长度
，并在循环中以固定比率递减，通常递减率设定为1.3。在一次循环中，梳子排序如同冒泡排序一样把阵列从首到尾扫描一次，比较及交
换两项，不同的是两项的间距不固定于1。如果间距递减至1，梳子排序假定输入阵列大致排序好，并以泡沫排序作最后检查及修正。
"""

from RandomList import random_list


def comb_sort(a):
    #compare_count = 0
    #swap_count = 0
    n = int(len(a))
    gap = n
    swapped = True
    while gap > 1 or swapped:
        if gap > 1:
            gap = int(gap / 1.3)
        #swapped = False
        for i in range(0, n-gap):
            #compare_count += 1
            if a[i] > a[i+gap] :
                a[i], a[i+gap] = a[i+gap], a[i]
                swapped = True
                #swap_count += 1
    #print("Compared %d, Swapped %d" % (compare_count, swap_count))
    return a


rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
comb_sort(rand_nums)
print("After Comb sort: ", len(rand_nums), rand_nums)
