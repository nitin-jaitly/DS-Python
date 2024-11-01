"""
Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[]= [0, 2, 1, 2, 0]
Output: 0 0 1 2 2
Explanation: 0s 1s and 2s are segregated into ascending order.
"""
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

def main():
    arr = [0, 2, 1, 2, 0]
    Sol = Solution()
    print(Sol.sort012(arr))
    assert Sol.sort012(arr) == [0, 0, 1, 2, 2]

if __name__ == "__main__":
    main()