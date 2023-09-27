import sys

def sortArry(arr):

	n = len(arr)
	counter_0 = 0
	counter_1 = 0
	counter_2 = 0

	print("Unsorted array = ", arr)
	for i in range(0, n):
		if arr[i] == 0:
			counter_0 += 1
		elif arr[i] == 1:
			counter_1 += 1
		elif arr[i] == 2:
			counter_2 += 1

	print("count for 0, 1 , and 2 are ", counter_0, counter_1, counter_2 )

	i = 0
	while counter_0 > 0:
		arr[i] = 0
		i += 1
		counter_0 -= 1

	while counter_1 > 0:
		arr[i] = 1
		i += 1
		counter_1 -= 1

	while counter_2 > 0:
		arr[i] = 2
		i += 1
		counter_2 -= 1

	print("Sorted Array = ", arr)


def drive_sort_array():
	A = [0,1,2,1,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,2,1,2,1,2,1,2,0,0]
	sortArry(A)


def selection_sort():
	A = [64, 25, 12, 22, 11]
	
	print ("Unsorted Array ", A)
	for i in range(len(A)):
		min_ind = 1
		
		## find the min element in remaining unsorted array
		for j in range(i+1, len(A)):
			if A[min_ind] > A[j]:
				min_ind = j
				
		## Swap the min element with the first element
		A[i], A[min_ind] = A[min_ind] , A[i]
		
		
	print("Sorted Array using Selection Sort \n ")
	for i in range(len(A)):
		print("%d" %A[i], end=' ')
		
		
#
# def bubble_sort(A):
# 	l = len(A)
#
# 	for i in range(n):
# 		for j in range(0 , n-i-1):
# 			if A[j] > A[j+1]:
#
