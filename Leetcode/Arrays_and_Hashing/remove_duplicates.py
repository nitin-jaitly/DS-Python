
"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = i + 1
    n = len(nums)

    print(nums)
    for i in range(n):
        if nums[i] == nums[j]:
            nums[i] = nums[j]
            i += 1

    print(nums)


def driver_removeDuplicates():

    nums = [0,1,2,3,3,4,4,5,5]

    removeDuplicates(nums)
