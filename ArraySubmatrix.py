"""
#Author: Yeswanth
#Date: 2024/03/30
#Learning: numpy
#Concept: Array Submatrix
"""
import numpy as np


def array_sub_matrix():
    my_list = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
    my_array = np.array(my_list)
    print(my_array)
    print()
    res = my_array[2:3, 2:3]
    print(res)


array_sub_matrix()
