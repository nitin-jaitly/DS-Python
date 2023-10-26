class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


def driver_contains_duplicate():
    nums = [1, 2, 3, 4, 5, 1, 3, 5]
    print("EEEEEE")
    print("the List A = ", nums, "Contains duplicate = ", Solution.containsDuplicate(Solution.containsDuplicate(nums)))
