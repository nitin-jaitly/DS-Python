
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
class Solution:
    def driver_find_primes(self):
        A = 30
        for number in range(1,A+1):
            if self.check_prime(number):
                    print(number, end=" ")

    def check_prime(self,number):
        for i in range(2, number + 1):
            if (number % i == 0) and (number != i) and (number != 1):
                return False
        return True

def main():
    sol = Solution()
    sol.driver_find_primes()

if __name__ == "__main__":
    main()

