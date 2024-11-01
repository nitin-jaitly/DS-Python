"""
There is a building with multiple floors. First floor has 10 flats numbered from 1 to 10.
2nd floor has 5 flats numbered from 11 to 15.
3rd floor has 10 flats numbered from 16 to 25.
4th floor has 5 flats numbered from 26 to 30.
5th floor has 10 flats again numbered from 31 to 40 and so on.
Write a python program to print the floor number if a flat number is given as input.
Ex: Enter the flat no.
26
Output: It belongs to 4th floor.
"""
#
# 1  - 1 to 10 -- 5         1/5 .. 4 ,, .. 3,  , 2, 1  , 0                          0
# 2 - 11 to 15 -- 10       12     11/15 11 , 12, 13, 14, 1                          0
# 3 - 16 to 25 -- 5 flats      16 to 25 ... 1 , 2, 3, 4, 0 , 1, 2, 3, 4 , 0 )       1
# 4 - 26 to 30 -- 5               26/15, 11 , 12 , 13, 14
# 5 - 31 to 40 -- 10
#
# [[] , [1,2,..10] , []]
#
# input = 27
# output = 4

def find_floor_given_flat_number(flat_number: int) -> int:

    if flat_number <= 0:
        return "Invalid flat number"

    floor = 1
    current_flat = 1

    while True:
        if floor % 2 != 0:
            flats_on_floor = 10
        else:
            flats_on_floor = 5

        if current_flat <= flat_number < current_flat + flats_on_floor:
            return f"It belongs to {floor}th floor"

        current_flat += flats_on_floor
        floor += 1

flat_number = int(input("Enter the flat number: "))
print(find_floor_given_flat_number(flat_number))
    #
    # quo = input // 5
    # reminder = input % 5
    #
    # floor = quo *
    # if (input % 5) in [1,2,3,4,0]:
    #     print("odd floor")
    # elif (input %5 ) in [1,14,13,12,11]:
    #     print("even floor ")
    #
