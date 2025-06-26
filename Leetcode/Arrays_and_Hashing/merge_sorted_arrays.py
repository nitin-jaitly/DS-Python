
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Solution
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Q2

Example 2: 
Input : A = [1, 2, 3, 5]
        B = [6, 7, 8, 9 ]
        C = [10, 11, 12]
Output: D = [1, 2, 3, 5, 6, 7, 8, 9. 10, 11, 12]

Given 3 arrays (A, B, C) which are sorted in ascending order, we are required to merge them together in ascending order and output the array D. 
Example 1: 
Input : C = [1, 2, 3, 4, 5] 
        B = [2, 3, 4]
        A = [4, 5, 6, 7]
Output : D = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7]

"""

"""
from Muralikrishna Dudaka to Everyone:    4:31  PM
- Given an array with 100 numbers
- array is not sorted
- 98 unique and 1 duplicate
- all the numbers are between 1-99
1 to 99 , 1 
find the sum of 1 to 99 ..  x  
 
 1 2 3  2 

SUm of 1 , 2 , 3 = 6 
Sum of 1 , 2 , 3, 2 = 8 .. 

8 - 6 = 2

find the sum of 1 to 100 indexes  .. y .
y - x

- Find the duplicate number
"""
from typing import List

def rev_string():
    A = "string"
    #rev_string = A[::-1]
    low = 0
    high = len(str) - 1
    while (low < high):
        if  str[low] != str[high]:

            return False
        low += 1
        high -= 1
    uppercase = str.upper()
    #streamlet

    return True

def merge_sorted_arrays( A, B, C):
    l1 = len(A)
    l2 = len(B)
    l3 = len(C)
    i, j , k = 0, 0, 0

    result = []
    while i < l1 or  j < l2  or  k < l3:
        if A[i] < B[j] and A[i] < C[j]:
            result.append(A[i])
        elif B[j] < A[i] and B[j] < C[k]:
            result.append(B[j])
        elif C[k] < A[i] and C[k] < B[j]:
            result.append(B[k])

        i += 1
        j += 1
        k += 1

    return result




def merge_sorted_arr(nums1: List[int], nums2: List[int]) -> None:
    m = len(nums1)
    n = len(nums2)

    i = m -1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >=0 :
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j>= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

def main():

    A = [4, 5, 6, 7, 0, 0, 0]
    B = [2, 3, 4]
    print("Before")
    print(A)
    print(B)
    merge_sorted_arr(A,B)
    print("After ")
    print(A)
    print(B)

if __name__ == "__main__":
    main()