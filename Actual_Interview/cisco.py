#
# Create a python function where input is string and output is dictionary which will produce letter frequency
#
# input_string = "Tech Mahindra"
#
# output_dicttionary = {'t' :1, 'e': 1, ...}
#
#


class Solution:

    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2

    def produce_letter_freq(self,input_str):
        my_dict = {}
        input_str = input_str.lower()
        for char in input_str:
            if char != ' ':
                if char not in my_dict:
                    my_dict[char] = 1
                else:
                    my_dict[char] += 1

        return my_dict

    def driver_produce_letter_freq(self):
        input_string = "Tech Mahindra"
        output_string = self.produce_letter_freq(input_string)
        print(output_string)

        l3 = self.l1 + self.l2
        print(l3)

        # for i in
        # l4 = l3.sort()
        # print(l4)


        # my_dict = {'t' :1, ''
        #            e': 1, ...}
        #assert

"""
l1 = [2, 354, 21, 67, 9, 20]
l2 = [576, 34, 67, 4, 0]
 
Add above two list and sort the added list. 
Note: For sorting don't use any inbuilt function.
"""


def main():
    l1 = [2, 354, 21, 67, 9, 20]
    l2 = [576, 34, 67, 4, 0]
    sol = Solution(l1,l2)
    sol.driver_produce_letter_freq()

if __name__ == "__main__":
    main()