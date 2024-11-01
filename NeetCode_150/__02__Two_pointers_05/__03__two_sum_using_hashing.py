
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        my_hash = {}

        for num in numbers:
            my_hash[num] = target - num

        for k, v in my_hash.items():
            if v in numbers:
                print(f"Found 2 sum for {target} using nums {k} and {v}")
                return [k, v]

        return False



    def driver_two_sum(self):
        numbers = [1, 3, 4, 5, 7, 10, 11]
        target = 9
        out = self.twoSum(numbers, target)
        print(self.twoSum(numbers, target))
        assert [4, 5] == self.twoSum(numbers, target)

def main():
    sol = Solution()
    sol.driver_two_sum()


if __name__ == "__main__":
    main()