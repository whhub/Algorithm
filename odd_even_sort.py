from RandomList import random_list


def odd_even_sort(a):
    is_sorted = False
    #compare_count = 0
    #exchange_count = 0
    n = len(a)
    while not is_sorted:
        is_sorted = True
        for i in range(1, n-1, 2):
            #compare_count += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                #exchange_count += 1
        for i in range(0, n-1, 2):
            #compare_count += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                #exchange_count += 1
    #print("Compared: %d, Exchanged: %d" % (compare_count, exchange_count))
    return a

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
odd_even_sort(rand_nums)
print("After odd even sort: ", len(rand_nums), rand_nums)
