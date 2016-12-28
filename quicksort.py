
def sort_i(a, left, right):
    if left >= right:
        return

    base = a[left]
    j = right
    i = left
    while i < j:
        while j > left and a[j] > base:
            j -= 1
        while i <= right and a[i] <= base:  # here write as <, result to wrong anwser
            i += 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if left < j:  # avoid swap(left, left)
        a[left], a[j] = a[j], a[left]

    sort_i(a, left, j-1)
    sort_i(a, j+1, right)


def quicksort(a):
    n = int(len(a))
    sort_i(a, 0, n-1)
    return a


from RandomList import random_list

rand_nums = random_list()
print("Before sort: ", len(rand_nums), rand_nums)
quicksort(rand_nums)
print("After  sort: ", len(rand_nums), rand_nums)
