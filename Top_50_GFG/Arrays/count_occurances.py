
def countOccurances(arr, n , x):

    count = 0
    for i in range(1, n ):
        if x == arr[i]:
            count += 1

    return count


def driver_count():
    A = [1, 1, 1, 1, 4, 4, 2, 6, 7, 11, 2]
    n = len(A)
    x = 1
    print("No of timees ", x, " occurs is ", countOccurances(A, n, x))
