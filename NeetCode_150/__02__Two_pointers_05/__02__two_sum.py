class Solution:
    def twoSum(self, numbers:list[int], target: int) -> list[int]:
            l , r = 0, len(numbers) - 1

            while l < r:
                if numbers[l] + numbers[r] < target:
                    l += 1
                elif numbers[l] + numbers[r] > target:
                    r -= 1
                elif numbers[l] + numbers[r] == target:
                    return [l+1, r+1]

    def driver_twoSum(self):
        numbers = [ 1,3,4,5,7,10,11]
        target = 9

        print(self.twoSum(numbers, target))