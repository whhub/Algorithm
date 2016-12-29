# global compare_count
# global swap_count
# compare_count = 0
# swap_count = 0


def sort_i(a, left, right):
    # global compare_count
    # global swap_count
    if left >= right:
        return

    base = a[left]
    j = right
    i = left
    while i < j:
        # compare_count += 1
        while j > left and a[j] > base:
            j -= 1
        # compare_count += 1
        while i <= right and a[i] <= base:  # here write as <, result to wrong anwser
            i += 1
        if i < j:
            # swap_count += 1
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if left < j:  # avoid swap(left, left)
        # swap_count += 1
        a[left], a[j] = a[j], a[left]

    sort_i(a, left, j-1)
    sort_i(a, j+1, right)


def quicksort(a):
    # global compare_count
    # global swap_count
    n = int(len(a))
    sort_i(a, 0, n-1)
    # print("Compared: %d, Swapped: %d" % (compare_count, swap_count))
    return a


from RandomList import random_list

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
quicksort(rand_nums)
print("After  sort: ", len(rand_nums), rand_nums)
