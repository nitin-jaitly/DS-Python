
def find_repeating_element(arr, n):
    dup = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                print("Found repeating element \n")
                return i
    # if no repeating element is found
    return -1


def find_repeating_using_hash(arr, n):
    # initialize index of first repeating element
    min = -1

    my_dict = {}

    for i in range(n-1, -1, -1):
        if arr[i] in my_dict.keys():
            min = i
        else:
            my_dict[arr[i]] = 1

    if min != -1:
        print("First repeating element = ", arr[min])
    else:
        print("No repeating elements ")

    return arr[min]


def driver_find_repeating():

    arr = [1, 3, 4, 5, 6, 7, 3, 5, 6, 7, 8, 8, 9]
    n = len(arr)

    index = find_repeating_element(arr, n)

    if index == -1:
        print("No repeating element found")
    else:
        print("Found repeating element at ", index, "is ", arr[index])

    repeating_element = find_repeating_using_hash(arr, n)
    print("Repeating element using hash = ", repeating_element)
