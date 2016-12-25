from RandomList import random_list


def bubble_sort(a):
    #did_swap = False
    #compare_count = 0
    #exchange_count = 0
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            #compare_count += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                #exchange_count +=1
                #did_swap = True
        #if not did_swap:
            #break
    #print("Compared : %d, Exchanged: %d" % (compare_count, exchange_count))
    return a

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
bubble_sort(rand_nums)
print("After Bubble sort: ", len(rand_nums), rand_nums)
