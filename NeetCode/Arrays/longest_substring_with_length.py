
def find_longest_substr(arr):
    n = len(arr)
    substr_len , max_len = 0, 0
    current = set()

    left, right = 0, 0

    while right < n:
        if arr[right] not in current:
            current.add(arr[right])
            substr_len = right - left
            max_len = max(substr_len, max_len)
            right += 1
            print("current = ", current)
        else:
            current.remove(arr[left])
            left += 1
    return max_len, current


def driver_longest_substring():
    A = "paloaltonetworks"
    length , substr = find_longest_substr(A)
    print("Longest substr is ", substr , "with length", length )
