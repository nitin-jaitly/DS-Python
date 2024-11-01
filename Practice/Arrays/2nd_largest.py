
"""
Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
"""
def second_largest(arr):
    arr = sorted(arr, reverse=True)
    print(arr)
    return (arr[1])
def main():
    arr = [12, 35, 1, 10, 34, 1]
    assert second_largest(arr) == 34

if __name__ == "__main__":
    main()