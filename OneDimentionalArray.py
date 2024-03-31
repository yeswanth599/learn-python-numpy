"""
#Author: Yeswanth
#Date: 2024/03/30
#Learning: numpy
#Concept: One Dimentional Array
"""

import numpy as np


def one_dimentional_array():
    read_n = int(input("Enter Array Size : "))
    create_array = np.ndarray(shape=read_n, dtype=int)
    print("enter %d elements" % read_n)
    for i in range(read_n):
        create_array[i] = input()
    print(create_array)


one_dimentional_array()
