
def get_min(arr, n):
	res = arr[0]
	for i in range(1, n):
		res = min(res, arr[i])
	return res
	

def get_max(arr, n):
	res = arr[0]
	for i in range(1, n):
		res = max(res, arr[i])
		return res
	

def driver_min_max():
	arr = [12, 234, 222 , 43, 24, 2, 4]
	n = len(arr)
	
	print("Min for arr", arr, " is ", get_min(arr,n))
	print("Max for arr", arr, " is ", get_max(arr,n))


def get_min(arr,n):
	min = arr[0]
	for i in range(1,n):
		if arr[i] < min:
			min = arr[i]
	return min

def get_max(arr,n):
	res = arr[0]
	for i in range(1,n):
		res = max(arr[i], res)
		
		