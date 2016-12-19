"""
Generate a random list ( 0-100)
"""

import random


def random_list():
    count = random.randint(10, 100)
    num_list = random.sample(range(100), count)
    return num_list


nlist = random_list()
print(nlist.__len__(), nlist)

