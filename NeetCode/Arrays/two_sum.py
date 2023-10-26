# class Solution:
#
#     def __init__(self, list, target):
#         self.list = list
#         self.target = target

def twoSum(nums: list[int], target: int) -> list[int]:
    my_dict = {}

    for i, v in enumerate(nums):
        diff = target - v
        if diff in my_dict:
            return [my_dict[diff], i]
        my_dict[v] = i


def driver_two_sum():
    A = [2, 4, 5, 6, 7, 9, 11]
    target = 12
    print("Indices for two sum = ", twoSum(A,target))
