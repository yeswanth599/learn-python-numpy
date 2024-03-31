"""
#Author: Yeswanth
#Date: 2024/03/31
#Learning: numpy
#Concept: Statistics - Standard Deviation
"""
import numpy as np


def mean_cal(list_array):
    return np.average(list_array)


def variance_cal(list_array):
    mean_of_list = mean_cal(list_array)
    for i in range(len(list_array)):
        list_array[i] = np.square(list_array[i] - mean_of_list)
    variance_of_list = np.average(list_array)
    print()
    print("Mean: ", mean_of_list)
    print("Variance: ", variance_of_list)
    return variance_of_list


# Standard deviation calculation based on list of elements
def standard_deviation_cal(list_elements):
    # converting list of elements to array of elements using numpy lib.
    list_array = np.array(list_elements)
    variance_list = variance_cal(list_array)
    standard_deviation = np.sqrt(variance_list)
    print("Standard Deviation: ", standard_deviation)


list_elements_input = [2, 4, 4, 4, 5, 5, 7, 9]
standard_deviation_cal(list_elements_input)
