"""
#Author: Yeswanth
#Date: 2024/03/30
#Learning: numpy
#Concept: Array Creation
"""

import numpy as np


class ArrayCreation:
    def array_creation(self):
        my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        my_arry = np.array(my_list)
        print("Complete Array")
        print(my_arry)

        print("Array Row Wise")
        for row in my_arry:
            print(row)

        print("Array Row element Wise")
        for row in my_arry:
            for row_ele in row:
                print(row_ele, end=' ')
            print()



array_creation_obj = ArrayCreation()
array_creation_obj.array_creation()
