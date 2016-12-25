from RandomList import random_list


def bubble_sort(a):
    did_swap = False
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                did_swap = True
        if not did_swap:
            break
    return a

rand_nums = random_list()
print("Before sort: ", rand_nums)
bubble_sort(rand_nums)
print("After Bubble sort: ", rand_nums)
