
def check_is_happy_number():
	nums = [2,28, 10, 5, 100]
	
	print("\n\n")
	for i in range(0,len(nums)):
		print("Case ", i+1 , " Numbers to check are " , nums[i])
		is_true = is_happy_number(nums[i])
		if is_true == True:
			print(nums[i] , " is a Happy Number")
		else:
			print(nums[i] , " is not a happy number")
		print("\n\n\n")


def sum_of_squared_digits(number):
	total_sum = 0
	while number > 0:
		number, digit = divmod(number, 10)
		total_sum += digit ** 2
	print("\t\tSum of squared digits: ", total_sum)
	return total_sum

def is_happy_number(n):
    # Helper function that calculates the sum of squared digits.
    slow_pointer = n  # The slow pointer value
    print("\tSetting slow pointer = input number", slow_pointer)
    print("\tSetting fast pointer = sum of squared digits of ", n, sep="")
    fast_pointer = sum_of_squared_digits(n)  # The fast pointer value
    print("\tFast pointer:", fast_pointer)
    while fast_pointer != 1 and slow_pointer != fast_pointer:  # Terminating condition
        print("\n\tRepeatedly updating slow and fast pointers\n")
        # Incrementing the slow pointer by 1 iteration
        slow_pointer = sum_of_squared_digits(slow_pointer)
        print("\t\tThe updated slow pointer is", slow_pointer, "\n")
        # Incrementing the fast pointer by 2 iterations
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))
        print("\t\tThe updated fast pointer is ", fast_pointer, "\n")
    # If 1 is found then it returns True, otherwise False
    if(fast_pointer == 1):
        print("\tSince fast pointer has converged to 1, the input number is a happy number.\n")
        return True
    print("\tFast pointer has not converged to 1, the input number is not happy number.\n")
    return False
		

def print_string_with_markers(strn, pValue):
    out = strn[:pValue] + '«' + strn[pValue] + '»' + strn[pValue+1:]
    return out