
def find_m_in_list(myList):
	print("List = ")
	l = len(myList)
	print(myList)
	l_sum = 0
	r_sum = 0
	left  = 0
	right = l - 1
	r_sum_list = []
	l_sum_list = []
	
	while ( left < l ):
		print(myList[left] , myList[right], "\n")
		l_sum = l_sum + myList[left]
		r_sum = r_sum + myList[right]
		# print("current_lsum = ", l_sum, "current rsum = ", r_sum)
		# print("current left index = ", left, "current right index = ", right)
		l_sum_list.append(l_sum)
		r_sum_list.append(r_sum)
		if l_sum in r_sum_list:
			# print("LSUM = ", l_sum)
			# print("RSUM = ", r_sum)
			print("left index = ", left)
			print("right index = ", right)
			print(" M = ", left + 1, "th Element where left sum is same as right sum ")

		#print(l_sum_list , r_sum_list, "\n")
		left += 1
		right -= 1
		
def find_element(myList):
	l = len(myList)
	l_sum = r_sum = 0
	m = 0
	print(myList)
	for i in range(1, l):
		l_sum = sum(myList[0:i])
		r_sum = sum(myList[i:])
		# print("i = ", i , "lsum = ", l_sum, "rsum = ", r_sum)
		# print("left_elem = " , myList[i])
		if l_sum == r_sum:
			print("Found m as ", i,  "th Element where lsum = rsum")
			m = i
			return m
		
def check_for_m_in_list():
	
	A = [ 2,3,4,5,6,9,8,3]
	mylist = A
	#find_m_in_list(mylist)
	find_element(A)
	
	B = [1,2,3,3,2,1]
	find_element(B)
	
	C = [-1,-2,-3,5,1,0]
	find_element(C)
	find_m_in_list(C)