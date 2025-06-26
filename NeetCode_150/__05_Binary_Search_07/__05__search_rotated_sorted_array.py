
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[left] < nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # Right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def main():
    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    assert 4 == search(nums,target)

    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    assert -1 == search(nums, target)



if __name__ == "__main__":
    main()





