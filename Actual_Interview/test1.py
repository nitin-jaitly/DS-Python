
"""
L = [3,0,0,2,0,4]

L has a coulum count .

0  0  0  0  0  1
1  0  0  0  0  1
1  0  0  1  0  1
1  0  0  1  0  1


"""



class Solution:
    def water_bound(self,L : list[int]) -> int:
        find_level = min(L[0], L[-1])
        # expected = 3

        sum = 0
        for value in L:
            if value == 0:
                sum = sum + find_level

            if value < find_level and value != 0:
               sum = sum + ( find_level - value)

        return sum

    def driver_water_bound(self):
        L = [3, 0, 0, 2, 0, 4]

        L = [3, 0, 0, 2, 0, 0, 10 , 20 , 0, 4, 1 , 0  , 0]

        left, right = 3, 0 #min


        print(self.water_bound(L))

#
# /Approach 2 .
# L = [3,0,0,2,0,4]
#
# if 0 then add 3
# if 0 then add 3
# if 0 then add 3 .
#
# 3 -2  = 1 , add 1 .
#
# Sum = 10
#
# Y               0  0  0  0  0  1  -> Level 4
# |               1  0  0  0  0  1  -> Level 3          .. Level 3 , Min ( 3, 4 ) = 3
# |               1  0  0  1  0  1  -> Level 2
# |____> X axis   1  0  0  1  0  1  -> Level 1
# i , j  i is x coor , j is y cord
#
#
# 1st Requirement , is to make sure that the water is within boundary.
# water_matrix[i , 0] and water_matrix[i, 5]
#
# Figure out till what level water can be filled up , In our case I has to be 0 , and 1 , and 2 .
#
# Then iternatte through 0, 0 to  2 , 5 check for 0  ,and increase count.
#
# Output = 10
#
#
# def
#

## Create a excel columns
#
# A   B   C  D .... Z
# AA  AB  AC        AZ
# ........................ZZ
#
# Length = 2
#
# A to ZZ
#
# Length = 3
# A to ZZZ
#
# list_of_chars = ['A', 'B', 'C', 'D' , .... 'Z']

def gen_length(input_length):

    solution = []

    initial_len = 1
    # while initial_len <= input_length:
    #     # for char in list_of_chars:
    #     #     solution.append(char)
    #     append_char()
    #
    #     for char in list_of_chars:
    #         for char2 in list_of_chars:
    #             solution.append(char, char2)
    #
    #     for char in list_of_chars:
    #         for char2 in list_of_chars:
    #             for char3 in list_of_chars:
    #                 solution.append(char, char2, char3)
    #
    # A B C
    #
    # A B C .
    #
    # AA AB AC
    #
    # BA BB BC
    #
    # CA CB CC
    #

    while initial_length < input_length:
        # for char in list_of_chars:
        #     solution.append(char)
        #
        solution = []
        for char in list_of_chars:
            for char2 in solution:
                result = str(char) + str(char2)

                solution.append(result)







