
"""
Compute the length of the longest strictly increasing subsequence in a list.
Input: nums = [11, 5, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
from bisect import bisect_left

def length_of_longest_sub(nums):
    if not nums:
        return 0

    my_list = []
    for num in nums:
        position = bisect_left(my_list, num)
        if position == len(my_list):
            my_list.append(num)
        else:
            my_list[position] = num
    print("nums = ", nums)
    print("my_list = ", my_list)
    return len(my_list)

def main():
    nums = [11, 5, 2, 5, 3, 7, 101, 18]
    print(length_of_longest_sub(nums))
if __name__ == "__main__":
    main()