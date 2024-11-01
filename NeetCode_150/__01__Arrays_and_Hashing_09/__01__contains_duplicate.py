from typing import List


class Solution:
    def containsDuplicate(self,nums: List[int]):
        seen = set()
        n = len(nums)
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate2(self, nums: list(int)):
        my_hash = {}
        for num in nums:
            my_hash[num] = 1 + my_hash.get(num, 0)

        for k, v in my_hash:
            if v > 1:
                return True
        return False

    def driver_contains_duplicate(self):
        nums = [1, 2, 3, 4, 5, 1, 3, 5]

        print(type(nums))
        print("EEEEEE")
        print("the List A = ", nums, "Contains duplicate = ", self.containsDuplicate(nums))

        print("the List A = ", nums, "Contains duplicate = ", self.containsDuplicate2(nums))

def main():
    sol = Solution()
    sol.driver_contains_duplicate()

if __name__ == "__main__":
    main()