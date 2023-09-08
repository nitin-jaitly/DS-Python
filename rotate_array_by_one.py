
def rotate(arr, n):
	x = arr[n - 1]
	for i in range(n-1, 0 , -1):
		arr[i] = arr[i - 1]
	arr[0] = x


def check_rotation():
	print_hi('PyCharm')
	
	arr = [1, 2, 3, 4, 5, 6, 7]
	n = len(arr)
	
	for i in range(0, n):
		print(arr[i], end=' ')
		print("range index = " + f'{i}')
	
	rotate(arr, n)
	
	print(" \n Rotated array is \n")
	for i in range(0, n):
		print(arr[i], end=' ')
		

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
