
"""
Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1].

Examples:

Input: n = 4, arr[] = [0,3,1,2]
Output: -1
Explanation: There is no repeating element in the array. Therefore output is -1.

Input: n = 5, arr[] = [2,3,1,2,3]
Output: 2 3
Explanation: 2 and 3 occur more than once in the given array.
"""

from typing import List


class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        my_hash = {}
        dups = []
        print(arr)
        for num in arr:
            my_hash[num] = 1 + my_hash.get(num, 0)
        #
        # print("Items in hash")
        # for k,v in my_hash.items():
        #     print("key = ",k ," value = ", v)

        dups_found = False
        for k, v in my_hash.items():
            if v > 1:
                dups.append(k)
                dups_found = True
        if dups_found == False:
            return -1
        return sorted(dups)
# {
# Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = IntArray().Input(n)
        obj = Solution()
        res = obj.duplicates(n, arr)

        print(res)
        #IntArray().Print(res)

# } Driver Code Ends