
def driver_binary_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print("arr = " + str(nums))
    index = binary_search(nums, target)
    print("Target " + str(target) + " for arr " + str(nums) + " found at index " + str(index))


def binary_search(nums: list, target) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            #print("element found at location mid = " + str(mid))
            return mid
    return -1

# practices
