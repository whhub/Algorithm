from RandomList import random_list


def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

rand_nums = random_list()
print("Before sort: ", rand_nums)
bubble_sort(rand_nums)
print("After Bubble sort: ", rand_nums)
