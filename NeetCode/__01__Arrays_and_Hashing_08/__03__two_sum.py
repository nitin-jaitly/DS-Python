# class Solution:
#
#     def __init__(self, list, target):
#         self.list = list
#         self.target = target

class Solution:
    def two_sum(self,nums: list[int], target: int) -> list[int]:
        prevMap = {}  # Val : index

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[v] = i

    def driver_two_sum(self):
        A = [2, 4, 5, 6, 7, 9, 11]
        target = 12
        print("Indices for two sum = ", self.two_sum(A, target))

        nums = [3, 2, 4]
        target = 6
        print("Indices for two sum = ", self.two_sum(nums,target))

        nums = [2, 7, 11, 15]
        target = 9
        print("Indices for two sum = ", self.two_sum(nums, target))

        nums = [3, 3]
        target = 6
        print("Indices for two sum = ", self.two_sum(nums, target))
