import sys

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
		
		
	print("Sorted Array \n ")
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
	