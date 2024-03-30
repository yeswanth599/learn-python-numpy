"""
#Author: Yeswanth
#Date: 2024/03/30
#Learning: numpy
#Concept: Array Properties
"""

import numpy as np


class ArrayProperties:
    def array_properties(self):
        my_list = [[10, 20, 30], [40, 50, 60]]
        my_array = np.array(my_list)
        print("Array : ", my_array)
        print("Array Properties")
        print("Array Size", my_array.size)
        print("Array Data Type", my_array.dtype)
        print("Array Dimentions", my_array.ndim)
        print("Shape of Array", my_array.shape)


array_properties_obj = ArrayProperties()
array_properties_obj.array_properties()
