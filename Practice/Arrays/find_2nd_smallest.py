
def find_2nd_smallest(my_list):

    smallest = float('inf')
    second_smallest = float('inf')

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return second_smallest

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_2nd_smallest(my_list))

    my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(find_2nd_smallest(my_list))

    my_list = [5,8,3,2,6]
    print(find_2nd_smallest(my_list))

if __name__ == "__main__":
    main()