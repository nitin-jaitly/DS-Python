
"""
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

"""

class Solution():
    def concat_array(self, A: list[int]) -> list[int]:
        for i in range(len(A)):
            A.append(A[i])

        return A

    def concat_array2(self,A):
        return(A + A)

    def driver_concat_array(self):
        A = [1,2,3,4,5]
        print(self.concat_array(A))
        print(self.concat_array2(A))


def main():
    sol = Solution()
    sol.driver_concat_array()

if __name__ == "__main__":
    main()