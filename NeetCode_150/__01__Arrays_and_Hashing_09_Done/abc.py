


"""

Write code to figure if a number is prime or not

Define Prime number
1 , 7 , 9 .

1 and 7 are primes because they are
1. divisible by 1
2. divisible by 7
and Not divisible by any number between 1 and 7
"""
#
#
# # Example 7.
# (1  , 7, )
#  2, 3, 4, 5,6)  ( 5 checks )
#
# ( 1, 9 )
# 2, ,3 4, 5, 6, 7, 8 ( 7 checks )
#
# 13
# # 2,3,4,5,6,7,8,9,10,11,12,13
# # Root of 13 ..
# # 3 to 4 + 1 .
# # 17   4 * 4 = 16   , 5 * 5 = 25
#
#
# def check_prime(number):
#     if even_number(number):
#         return False
#
#     for i in range(1,number+1):
#
#
#
#         if (number % i == 0) and (i != 1 ) and ( i != number):
#             return False
#     return True
#
#



class cube:
    def __init__(self,volume):
        self.volume = volume

    def __str__(self):
        return "volume is " + str(self.volume)

    def __add__(self, other):
        volume = self.volume + other.volume
        return cube(volume)

    def __mul__(self, other):
        volume = self.volume * other.volume
        return cube(volume)


