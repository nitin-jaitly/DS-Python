
import math

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:

    def subArraySum(self, arr, n, s):
        start = 0
        end = 0
        current_sum = 0

        for end in range(n):
            current_sum += arr[end]

            while current_sum > s and start <= end:
                current_sum -= arr[start]
                start += 1

            if current_sum == s:
                return [start + 1, end + 1]

        return [-1]


    def subArraySum2(self, arr, n, s):
        sum = 0
        for i, num in enumerate(arr):
            sum = num

            if sum == s:
                return [i + 1, i + 1]
            else:
                for j in range(i + 1, len(arr)):
                    sum += arr[j]
                    if sum == s:
                        return [i + 1, j + 1]
                    elif sum > s:
                        break
        return [-1]




def main():
    arr = [1, 2, 3, 7, 5]
    n = 5
    s = 12

    Sol = Solution()
    print(Sol.subArraySum(arr,n,s))
    assert Sol.subArraySum(arr, n, s) == [2, 4]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    s = 15
    print(Sol.subArraySum(arr,n,s))
    assert Sol.subArraySum(arr, n, s) == [1, 5]

    arr = [7, 2, 1]
    n = 3
    s = 2
    print(Sol.subArraySum(arr,n,s))
    assert Sol.subArraySum(arr, n, s) == [2, 2]

    arr = [5, 3, 4]
    n = 3
    s = 2
    print(Sol.subArraySum(arr,n,s))
    assert Sol.subArraySum(arr, n, s) == [-1]

    arr = [1, 2, 3, 4]
    n = 4
    s = 0
    print(Sol.subArraySum(arr,n,s))
#    assert Sol.subArraySum(arr,n,s) == [-1]

if __name__ == "__main__":
    main()
# } Driver Code Ends