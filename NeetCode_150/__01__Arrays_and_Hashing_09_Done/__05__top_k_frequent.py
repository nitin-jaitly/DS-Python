"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""

class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    print(f"nums = {nums}")
                    print(f"count = {count}")
                    print(f"freq = {freq}")
                    print(f"res = {res}")
                    return res

    def driver_top_k_frequent(self):
        nums = [1,1,1,1,3,4,5,6,5,5,2,6]
        k = 3
        print(self.top_k_frequent(nums, k))

def main():
    sol = Solution()
    sol.driver_top_k_frequent()

if __name__ == "__main__":
    main()