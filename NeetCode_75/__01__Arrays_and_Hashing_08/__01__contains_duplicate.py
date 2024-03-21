from typing import List


class Solution:
    def containsDuplicate(self,nums: List[int]):
        seen = set()

        n = len(nums)
        # for i in range(n):
        #     if nums[i] in seen:
        #         return True
        #     seen.add(nums[i])
        #
        # return False
        #
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


    def driver_contains_duplicate(self):
        nums = [1, 2, 3, 4, 5, 1, 3, 5]

        print(type(nums))
        print("EEEEEE")
        print("the List A = ", nums, "Contains duplicate = ", self.containsDuplicate(nums))
