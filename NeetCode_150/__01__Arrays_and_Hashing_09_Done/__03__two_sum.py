"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


"""
class Solution:
    def two_sum(self,nums: list[int], target: int) -> list[int]:
        prevMap = {}  # Val : index

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[v] = i

    def driver_two_sum(self):
        nums_list = [
            [2, 4, 5, 6, 7, 9, 11],
            [3, 2, 4],
            [2, 7, 11, 15],
            [3, 3]
        ]

        target_list = [12, 6, 9, 6 ]
        for i in range(len(nums_list)):
            print(f"\n\nindex i = {i}")
            print(f"nums_list of {i} index = {nums_list[i]}")
            print(f"target = {target_list[i]}")
            print("Indices for two sum = ", self.two_sum(nums_list[i], target_list[i]))

if __name__ == "__main__":
    sol = Solution()
    sol.driver_two_sum()