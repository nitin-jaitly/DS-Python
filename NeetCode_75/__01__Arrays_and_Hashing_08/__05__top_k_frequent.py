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
                    return count, freq, res


    def driver_top_k_frequent(self):
        nums = [1,1,1,1,3,4,5,6,5,5,2,6]
        k = 3
        print(self.top_k_frequent(nums, k))



