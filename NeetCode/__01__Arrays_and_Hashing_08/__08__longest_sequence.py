
class Solution:
    def longestConsecutiveSequence(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0
        seq = []

        for n in nums:
            ## Check if n is start of a sequence
            if (n - 1) not in numset:
                seq_length = 0
                while (n + seq_length) in numset:
                    seq_length += 1
                longest = max(seq_length, longest)
        return longest


    def driver_longest_seq(self):
        nums = [100, 4, 200, 5, 6, 7, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 1, 3, 2]
        sol = Solution
        longest = sol.longestConsecutiveSequence(self, nums)
        print("Longest seq = ", longest)

        nums = [100,4,200,1,3,2]
        longest = sol.longestConsecutiveSequence(self, nums)
        print("Longest seq = ", longest)

        nums = [0,3,7,2,5,8,4,6,0,1,55,23,21,22,24,25,26,27,28,29,30,31,32,33]
        longest = sol.longestConsecutiveSequence(self, nums)
        print("Longest seq = ", longest)

