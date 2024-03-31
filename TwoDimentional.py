"""
#Author: Yeswanth
#Date: 2024/03/30
#Learning: numpy
#Concept: Two Dimentional
"""

import numpy as np


def two_dimentioanl():
    print("Welcome to Two Dimentional Array")
    print()
    read_row = int(input("Enter Row Size: "))
    read_col = int(input("Enter Col Size: "))
    create_two_dim = np.ndarray(shape=(read_row, read_col), dtype=int)
    print("Array Size: ", create_two_dim.size)
    print("Array Dimention:", create_two_dim.ndim)
    print("Array Shape:", create_two_dim.shape)
    print("Please enter %d elements of %dX%d Matrix" % (read_row * read_col, read_row, read_col))
    print()
    for i in range(read_row):
        for j in range(read_col):
            create_two_dim[i][j] = input()
    print(create_two_dim)


two_dimentioanl()
