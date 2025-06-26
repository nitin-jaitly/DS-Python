from typing import List


class Solution:
    def containsDuplicate(self,nums: List[int]):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate2(self, nums: List[int]):
        my_hash = {}
        print(nums)
        for num in nums:
            my_hash[num] = 1 + my_hash.get(num, 0)
        print(f"my_hash = {my_hash}")
        for k, v in my_hash.items():
             if v > 1:
                 return True
        return False

    def driver_contains_duplicate(self):
        nums = [1, 2, 3, 4, 5, 1, 3, 5]
        E = "EEEEEE"
        print("the List A = ", nums, "Contains duplicate = ", self.containsDuplicate(nums))
        print("the List A = ", nums, "Contains duplicate = ", self.containsDuplicate2(nums))
        print("the list E = ", E, "contains dup = ", self.containsDuplicate(E))
        print("the list E = ", E, "contains dup = ", self.containsDuplicate2(E))

def main():
    sol = Solution()
    sol.driver_contains_duplicate()

if __name__ == "__main__":
    main()