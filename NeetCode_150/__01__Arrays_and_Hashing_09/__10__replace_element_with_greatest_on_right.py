"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

"""

class Solution:

    def replace_greatest_on_right(self, L: list[int]) -> list[int]:
        n = len(L)

        for i in range(len(L)):
            if L[i+1:n]:
                L[i] = max(L[i+1:n])

        L[n - 1] = -1
        return(L)


    def driver_replace_greatest_on_right(self):
        L = [17,18,5,4,6,1]
        # print("original list = " + str(L))
        expected = [18,6,6,6,1,-1]
        print("expected list \t= " + str(expected))
        actual = str(self.replace_greatest_on_right(L))
        print("actual list \t= " + str(actual))
        assert (str(actual) == str(expected))