import sys


def driver_selection_sort():
    print("Sorted Array")
    for i in range(len(A)):
        print("%d" % A[i], end=", ")

    A = [64, 25, 12, 22, 11]


def selection_sort(A):
    for i in range(len(A)):
        min_idx = 1
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
