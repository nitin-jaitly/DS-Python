
def maxSubArraySum(nums):
    max_so_far = float("-inf")
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here += nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

        return max_so_far


def main():
    arr = [1, 2, 3, -2, 5]
    print(maxSubArraySum(arr))


if __name__ == "__main__":
    main()
