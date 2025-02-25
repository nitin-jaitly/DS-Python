"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self,nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, element in enumerate(nums):
            ## Skip Duplicates
            if i > 0 and element == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = element + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([element, nums[l], nums[r]])
                    l += 1
                    ## Skip Duplicates
                    while  nums[l] == nums[l-1] and l < r:
                        l += 1
                    while  nums[r] == nums[r - 1] and l < r:
                        r -= 1
        return res


    def driver_three_sum(self,):
        A = [-3, 3, 4, -3, 1, 2]
        res = self.threeSum(A)
        print(res)


