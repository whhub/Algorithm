"""
Generate a random list ( 0-100)
"""

import random


def random_list():
    count = random.randint(10, 100)
    num_list = []
    for i in range(0, count):
        num_list.append(random.randint(0, 100))
    return num_list


nlist = random_list()
print(nlist.__len__(), nlist)

