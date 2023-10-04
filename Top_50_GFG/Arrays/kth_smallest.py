

def kthSmallest(arr, n, k):

    arr.sort()
    print("Sorted arr", arr)
    return arr[k-1]


def driver_kth_smallest():
    A = [1 , 4, 3 , 7, 8, 2, 6, 7, 111, 412 , 312, 143]
    k =11

    n = len(A)
    print("unsorted array  = ", A)
    smallest = kthSmallest(A, n, k)
    print("Kth Smallest = ", smallest)
