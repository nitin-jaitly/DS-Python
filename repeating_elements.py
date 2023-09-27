def repeating_elements():
    numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
    arr_size = len(numRay)
    print(numRay)
    for i in range(arr_size):
        x = numRay[i] % arr_size
        print("x =" , x)
        numRay[x] = numRay[x] + arr_size
        print("numRay[x] = ", numRay[x])

    print("The repeating elements are : ")
    for i in range(arr_size):
        if numRay[i] >= arr_size*2:
            print(i, " ")
    return None
