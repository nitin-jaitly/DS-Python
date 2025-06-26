"""
Given a list of non-negative numbers and a target integer k,
 check if the array has a continuous subarray of size at least 2 that sums up to k

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
"""

def check_array_for_sum2(nums, k) -> bool:
    for i, num in enumerate(nums):
        sum = num
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum == k:
                return True

    return False

def check_array_for_sum(nums, k) -> bool:
    # Create a dictionary to store the sum of elements in the array
    sum_dict = {}
    sum_dict[0] = -1
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        if k != 0:
            sum = sum % k

        if sum in sum_dict:
            if i - sum_dict[sum] > 1:
                return True
        else:
            sum_dict[sum] = i
    return False

def main():
    nums = [23, 2, 4, 6, 7]
    k = 6
    # print(check_array_for_sum2(nums , k))
    # assert check_array_for_sum2(nums, k) == True
    #
    # nums = [23 , 2, 10, 2 , 1, 1, 1, 0, 2, 5]
    # print(check_array_for_sum2(nums, k))
    # assert check_array_for_sum2(nums,k) == False
    #
    # nums = [2, 23, 4]
    # print(check_array_for_sum2(nums, k))
    # assert check_array_for_sum2(nums, k) == False
    # #
    A = [1, 2, 4]

    print(check_array_for_sum2(nums, k))
    assert check_array_for_sum2(nums, k) == True

if __name__ == "__main__":
    main()