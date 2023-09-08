def reverse_list(A, start, end):
	while (start < end):
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1


def drive_reverse_list():
	A = [1, 2, 4, 5, 6, 7, 9]

	n = len(A)
	start = 0
	end = n - 1
	print(A)
	reverse_list(A, start, end)
	print("reversed list = ", A)
	
	recurse_rev_list(A, start, end)
	print("Recured reversed list = ", A)


def recurse_rev_list(A, start, end):
	mid = ( start + end ) // 2
	print (mid)
	while start <= mid:
		if start > mid:
			return
		print("start  = ", start )
		print("mid = " , mid)
		print("end = " , end )
		print("Swapping , ", A[start] , A[end])
		A[start], A[end] = A[end], A[start]
		print(A)
		start += 1
		end -= 1
		print("new start = " , start)
		print("new end = ", end)
		print()
		
		recurse_rev_list(A, start, end)

