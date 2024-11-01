# User function Template for python3
class Solution:

    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):

        actual_sum = 0
        expected_sum = 0
        for i, num in enumerate(arr):
            print(num, end=" ")
            actual_sum += num

        for i in range(1, n + 1):
            expected_sum += i

        print("\nMissing number  = ", end = " ")
        missing_num = expected_sum - actual_sum
        return missing_num


def main():

    # {
    # Driver Code Starts
    # Initial Template for Python 3
    Sol = Solution()

    n = 5
    arr = [1, 2, 3, 5]
    print(Sol.missingNumber(n,arr))


if __name__ == "__main__":
    main()