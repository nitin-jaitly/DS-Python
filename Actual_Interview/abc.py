"""

from Muralikrishna Dudaka to Everyone:    4:06  PM
Given an array and a number k where k is smaller than the size of the array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.
Examples:
Input: arr[] = {7, 10, 4, 3, 20, 15}, k = 3
Output: 7
Input: arr[] = {7, 10, 4, 3, 20, 15}, k = 4
Output: 10

"""
#3 4 7 10 15 20

arr= [7, 10, 4, 3, 20, 15]
k = 3

def bin_search(arr, k, low, high):
    mid = low + high // 2


## find first three min in a list
def find_min(arr, k):
    first_min, second_min, third_min = 0, 0, 0
    for num in arr:
        if num < first_min:
            first_min = num
            second_min = first_min
            third_min = second_min
        elif num < second_min:
            third_min = second_min
            second_min = num
        elif num < third_min:
            third_min = num
    return first_min, second_min,third_min