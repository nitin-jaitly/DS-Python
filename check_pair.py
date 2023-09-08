
def check_for_pair(A , size , x):
	for i in range(0 , size - 1):
		for j in range(i+1, size - 2 ):
			if A[i] + A[j] == x:
				return 1
	return 0


## O(N^^2)
def test_check_pair():
	A = [ 0, -1, 2, -3, 1]
	x = -2
	size = len(A)
	
	if (check_for_pair(A,size, x)):
		print("Found ", x , " in array " , A)
	else:
		print("No")
		
		
def checkTwoSum( A, arr_size, sum):
	# Sort the Array
	print("in checkTwoSum")
	print(A)
	A.sort()
	print(A)
	l = 0
	r = arr_size - 1
	i = 0
	while i < arr_size - 1:
		searchKey = sum - A[i]
		if binary_search(A ,i + 1, r, searchKey) == 1:
			print("found")
			return 1
		i = i + 1
	return 0


def binary_search(A ,low, high, searchKey):
	mid = 0
	while low <= high:
		mid = high + low // 2
		if A[mid] == searchKey:
			return 1
		if A[mid] < searchKey:
			low = mid + 1
		if A[mid] < searchKey:
			high = mid - 1
	## if we reach here element is not present
	return 0



def test_checkTwoSum():
	A = [1,4,45,6,10,-8]
	n = 14
	if checkTwoSum(A, len(A), n):
		print("Yes")
	else:
		print("No")
		
		
def print_pairs(arr, arr_size, sum):
	hashmap = {}
	
	for i in range(0, arr_size):
		temp = sum - arr[i]
		if ( temp in hashmap):
			print("Yes")
			return 1
		hashmap[arr[i]] = i
	print("No")
	
def test_print_pairs():
	A = [1, 4, 45, 6, 10, 8]
	n = 16
	print_pairs(A, len(A), n)
	
	