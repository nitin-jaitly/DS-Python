from typing import List

# Binary search is a search algorithm that finds the position of a target value within a sorted array.
def binary_search(A: List, elem: int) -> bool:
    low = 0
    high = len(list(A)) - 1

    while low <= high:
        mid = ( low + high ) // 2
        if A[mid] == elem:
            return True
        elif elem > A[mid]:
            low = mid + 1
        elif elem < A[mid]:
            high = mid - 1
    return False

def find_common_elements(A: List, B: List) -> List:
    A.sort()
    B.sort()
    common_elements = []
    for elem in B:
        if binary_search(A, elem):
            common_elements.append(elem)
    return common_elements

def main():
    A = [2, 4, 5, 4, 6, 3, 99, 34, 21, 67, 32, 54, 87]
    B = [ 44, 66, 21,67, 99, 54]
    print (A, B)
    print(find_common_elements(A, B))

    X = list(set(A) - set(B))
    Y = list(set(B) - set(A))
    intersect = (list(set(A) & set(B)))
    union = (list(set(A + B)))
    intersect2 = list(set(union) - set( X + Y))

    intersect.sort()
    intersect2.sort()
    print(intersect2)
    print(intersect)
    assert intersect == intersect2 == find_common_elements(A, B)

if __name__ == "__main__":
    main()