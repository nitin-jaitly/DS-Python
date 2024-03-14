
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Solution
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

"""

from typing import List

def merge_sorted_arr(nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    m = len(nums2)
    nums3 = List[int]

    i = n - 1
    j = m - 1
    k = n + m - 1

    while i >= 0 and j >=0 :
        if nums1[i] > nums2[j]:
            nums3[k] = nums1[i]
            i -= 1
        else:
            nums3[k] = nums2[j]
            j -= 1

        k -= 1


    while j>= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


