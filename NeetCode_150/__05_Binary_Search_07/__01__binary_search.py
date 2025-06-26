
def driver_binary_search():
    nums = [-1, 0, 3, 5, 9, 12, 32 , -4, -5]
    target = -4
    print("arr = ", nums)
    index = binary_search(nums, target)
    print("Target " + str(target) + " for arr " + str(nums) + " found at index " + str(index))


def binary_search(nums: list, target) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    mid = 0

    nums.sort()
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

def main():
    driver_binary_search()

if __name__ == "__main__":
    main()