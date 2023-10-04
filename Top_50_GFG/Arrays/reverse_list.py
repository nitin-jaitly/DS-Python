

def reverse_list(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def driver_reverse_list():
    arr = [ 1, 3, 5, 6, 3, 2, 1, 7, 8, 11, 21, 45, 12, 4]
    n = len(arr)
    print("Arr = ", arr)

    rev = reverse_list(arr, start=0 , end= n-1)
    print("revered list = ", rev)

