
def longestConsecutiveSequence(nums: list[int]) -> int:
    numset = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numset:
            seq_length = 0
            while ( n + seq_length) in numset:
                seq_length += 1
            longest = max(seq_length, longest)
    return longest


def driver_longest_seq():
    A = [100, 4, 200, 5, 6, 7, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 1, 3, 2]
    longest = longestConsecutiveSequence(A)
    print("Longest seq = ", longest)



