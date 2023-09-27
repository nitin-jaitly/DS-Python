
def find_array_occurance(A , n , x):
    res = 0
    for i in range(0, n ):
        if A[i] == x:
            res += 1

    return res


def driver_occur():

    A = [0, 1, 2, 4, 5, 6, 4, 2, 2, 3, 4, 6, 7, 9]
    x = 2
    n = len(A)
    res = find_array_occurance(A, n, x)

    print("For the list ", A , "occurred element ", x , res, "times")


def binary_search(arr, l, r, x):
    if r < l:
        return -1

    mid = int(l + (r - 1)  /  2)

    if arr[mid] == x:
        return mid

    if arr[mid] > x:
        return binary_search(arr, l, mid-1, x)

    if arr[mid] > x:
        return binary_search(arr, mid+1, r, x)


