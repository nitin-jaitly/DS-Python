def find_peak(arr, n):
	if n == 1:
		return 0
	if arr[0] >= arr[1]:
		return 0
	if arr[n - 1] >= arr[n - 2]:
		return n - 1
	
	# check for every other element
	for i in range(1, n - 1):
		if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
			return i


def driver_find_peak():
	arr = [1, 3, 20, 4, 1, 0]
	n = len(arr)
	print("Index of a peak is ", find_peak(arr, n))
