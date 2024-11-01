

def sort_and_remove_dup(input):

    seen = set()
    result = []
    for elem in input:
        if elem not in seen:
            result.append(elem)
    return result


    #
    # new_list = list(set(input))
    # new_list.sort()
    #
    # input = [1, 2, 7, 4, 3, 2, 1, 8, 9]




def main():

    input = [1, 2, 7, 4, 3, 2, 1, 8, 9]
    print(sort_and_remove_dup(input))
    ##ouptut = {1, 2, 3, 4, 7, 8, 9}, length =

if __name__ == "__main__":
    main()