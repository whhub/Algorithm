from RandomList import random_list


def cocktail_sort(a):
    compare_count = 0
    exchange_count = 0
    n = len(a)
    for i in range(int(n / 2)):
        for j in range(i, n-1-i):
            compare_count += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                exchange_count += 1
        for j in range(n-1-i, i, -1):
            compare_count += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange_count += 1
    print("Compared: %d, Exchanged: %d" % (compare_count, exchange_count))
    return a


rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
cocktail_sort(rand_nums)
print("After cocktail sort: ", len(rand_nums), rand_nums)

