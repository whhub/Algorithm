"""
#coding=utf8

侏儒排序（Gnome Sort）

也叫地精排序、Stupid Sort，号称写出来最简单的排序代码，它很像冒泡，也是通过一系列的元素交换完成的。这个算法你初看起来
只有一层循环，但是实际上它的游标却并不总是往前进的，有时需要后退，所以总的时间复杂度并不小。这个算法总是能够找到第一组
大小顺序错误的毗邻元素，然后交换它们。但是交换这两个元素的时候，又可能会带来新的顺序错误的毗邻元素对，所以在交换元素
之后需要重新检查影响到的毗邻元素。
"""


def gnome_sort(a):
    #compare_count = 0
    #swap_count = 0
    pos = 1
    n = int(len(a))
    while pos < n:
        #compare_count += 1
        if a[pos] >= a[pos-1]:
            # 毗邻元素顺序正确，前进
            pos += 1
        else:
            #swap_count += 1
            a[pos], a[pos-1] = a[pos-1], a[pos]
            if pos > 1:   # 交换元素可能会带来新的毗邻元素顺序错误
                pos -= 1
    #print("Compared:%d, Swapped:%d" % (compare_count, swap_count))
    return a


from RandomList import random_list

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
gnome_sort(rand_nums)
print("After Gnome sort: ", len(rand_nums), rand_nums)
