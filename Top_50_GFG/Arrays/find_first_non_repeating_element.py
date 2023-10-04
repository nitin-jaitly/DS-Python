from collections import defaultdict


def find_first_non_repeating_element(arr, n):
    my_dict = defaultdict(lambda: 0)

    for i in range(n):
        my_dict[arr[i]] += 1

    print(my_dict)

    for i in range(n):
        if my_dict[arr[i]] == 1:
            print("First non repeating element =", arr[i])
            return arr[i]


def driver_find_first_non_repeating_element():
    arr = [1, 1, 1, 2, 3, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 8, 9]
    n = len(arr)
    nre  = find_first_non_repeating_element(arr, n)
    print("First non repeating element = ", nre)


