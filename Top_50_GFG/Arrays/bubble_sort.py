
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                ##Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if (swapped == False):
            break


def driver_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted Array")
    print(arr)
    bubble_sort(arr)
    print("Sorted Array")
    for i in range(len(arr)):
        print("%d" %arr[i], end=" ")
