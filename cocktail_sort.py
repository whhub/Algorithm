from RandomList import random_list


def cocktail_sort(a):
    n = len(a)
    for i in range(int(n / 2)):
        for j in range(i, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        for j in range(n-1-i, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

rand_nums = random_list()
print("Before sort: ", rand_nums)
cocktail_sort(rand_nums)
print("After cocktail sort: ", rand_nums)
