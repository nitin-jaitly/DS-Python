
def find_peak(arr, n):
    if n == 1:
        return 0

    if arr[0] >= arr[1]:
        return 0

    if arr[n - 1] >= arr[n - 2]:
        return n - 1

    for i in range(1, n):

        if (arr[i+1] > arr[i]) and (arr[i-1] < arr[i]):
            print("Found the Peak Element as ", arr[i], "At position", i)
            return arr[i], i


def driver_find_peak():
    arr = [1, 3, 20, 4, 1, 0]
    n = len(arr)

    elem, index = find_peak(arr, n)
    print("Index, index at peak number", elem)
