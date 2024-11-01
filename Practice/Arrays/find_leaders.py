class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def find_leaders(self, n, arr):
        # Code here
        leader = 0
        leaders = []
        max_from_right = arr[-1]
        leaders.append(max_from_right)

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders.append(max_from_right)
        #leaders = list(set(leaders))
        # print("arr = ",arr)
        # print("leaders = ", leaders)
        # print(sorted(leaders,reverse=True))
        return sorted(leaders,reverse=True)

# {
# Driver Code Starts
# Initial Template for Python 3

import math

def main():
    Sol = Solution()
    arr = [16, 17, 4, 3, 5, 2]
    n = len(arr)
    print(Sol.find_leaders(n,arr))

    assert Sol.find_leaders(n,arr) == [17, 5, 2]


#
# def main():
#     T = int(input())
#
#     while (T > 0):
#
#         N = int(input())
#
#         A = [int(x) for x in input().strip().split()]
#         obj = Solution()
#
#         A = obj.leaders(N, A)
#
#         for i in A:
#             print(i, end=" ")
#         print()
#
#         T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends