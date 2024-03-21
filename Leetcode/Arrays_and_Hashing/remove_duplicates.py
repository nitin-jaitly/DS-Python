
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

class Solution:
    def removeDuplicates(self,nums: List[int]) -> int:
        i = 0
        j = i + 1
        n = len(nums)

        print(nums)
        for i in range(n):
            if nums[i] == nums[j]:
                nums[i] = nums[j]
                i += 1

        print(nums)

    def removeDuplicates_2(self,nums: List[int]) -> int:
        my_hash = {}

        for num in nums:
            my_hash[num] = 1 + my_hash.get(num, 0)

        for key, value in my_hash.items():
            if value > 1:
                nums.remove(key)

        return nums


    def removeDuplicates_3(self, nums: List[int]) -> int:
        return list(set(nums))

    def removeDuplicates_4(self, nums: List[int]) -> int:
        seen = []

        for num in nums:
            if num not in seen:
                seen.append(num)

        return seen

    def driver_removeDuplicates(self):
        nums = [0,1,2,3,3,4,4,5,5]
        print(nums)
        print(self.removeDuplicates_4(nums))

        print(self.removeDuplicates_3(nums))

        print(self.removeDuplicates_2(nums))

        print(self.removeDuplicates(nums))