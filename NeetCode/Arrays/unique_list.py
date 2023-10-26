
def unique_list(nums, n):
    nums_unique = []

    # for i in range(n):
    #     if nums[i] not in nums_unique:
    #         nums_unique.append(nums[i])

    nums_unique = list(set(nums))
    return nums_unique


def driver_unique():

    A = [1, 1, 1, 1, 1, 1, 13, 3, 3, 3, 5, 32, 2, 2, 4, 7, 8, 3, 2, 4, 3]
    print("Not unique list =", A)
    print("Unique list     =", unique_list(A,len(A)))

