"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

 """
import itertools
import collections
class Solution:
    def sliding_window(self, nums: list[int], k : int ) -> list[int]:

        l , r = 0 , k - 1
        sliding_window = []
        max_sliding_window = []

        while r < len(nums):
            sliding_window = nums[l:r + 1]
            max_val = max(sliding_window)
            max_sliding_window.append(max_val)
            l += 1
            r += 1

        print("actual sliding window = \t" + str(max_sliding_window))
        return max_sliding_window

    def sliding_window_2(self, nums: list[int], k : int ) -> list[int]:

        l, r = 0, k - 1
        sliding_window = []
        max_sliding_window = []

        sliding_window = nums[l:r + 1]
        current_max = max(sliding_window)

        while r < len(nums):
            current_max = max(current_max, nums[r])
            max_sliding_window.append(current_max)
            l += 1
            r += 1

        return max_sliding_window

    def max_sliding_window_3(self, nums: list[int], k: int) -> list[int]:
        l = r = 0
        q = collections.deque()
        output = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()

            if r + 1  >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

    def driver_sliding_window(self):
        # nums = [[1, 3, -1, -3, 5, 3, 6, 7],
        #         [1],
        #         [1,2,3,4,5,6,7,8],
        #         ]
        #
        # k = [3, 1, 4]
        #
        # expected = [[3, 3, 5, 5, 6, 7],
        #             [1],
        #             [4,5,6,7,8]]

        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]

        print("nums = " , str(nums))
        print("Expected sliding window = \t" + str(expected))
        print("Actual sliding window = \t" + str(self.max_sliding_window_3(nums, k)))
        assert expected == self.max_sliding_window_3(nums, k)

        # for (x, y, z) in itertools.zip_longest(nums, k, expected):
        #     print(x , y, z)

        # for (num_list, k_value), expected_list in zip(zip(nums ,k), expected):
        #     print("\n")
        #     print(num_list)
        #     print(k_value)
        #     print(expected_list)
        #     #print(expected_list)
        #
        #     nums = num_list
        #     k = k_value
        #     expected_values = expected_list
        #
        #     print("Expected sliding window = \t" + str(expected_values))
        #     assert expected_values == self.sliding_window_3(nums, k)

        exit()




