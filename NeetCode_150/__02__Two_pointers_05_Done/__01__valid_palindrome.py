import curses.ascii


#
# "NITIN"
#
#  Ignore other chars..
#
#  char in question is .. charcter c .
#
#     ord('A') =< ord(c)
#     curses.ascii.isalpha()
#   A - Z
#   a - z
#   0 - 9
#
#   ID , EMAIL
#   01 , nitin@exabeam.com
#   02,  nitin@exabeam.com
#   03,  nitin@exabeam.com
#   04,  nitin5@exabeam.com
#   05,  nitin6@exabeam.com
#
#   select id , email from table1
#   group by email
#   having count(email) > 1

class Solution:
    def driver_check_palindrome(self):
        string = "“M a    ; _ d    ;;  — A m"
        string = "N I TIN"
        string = "\"A man, a plan, a canal: Panama\""
        print("The string " + string + " is a Palindrome ? " + str(self.isPalindrome(string)))

    def isPalindrome(self, arr):
        arr = arr.lower()
        n = len(arr)
        left = 0
        right = n - 1
        while left < right:
            while left < right and not self.check_if_alpha(arr[left]):
                left += 1

            while left < right and not self.check_if_alpha(arr[right]):
                right -= 1

            if arr[left] != arr[right]:
                return False
            right -= 1
            left += 1
        return True

    def is_palindrome2(self, arr):
        left = 0
        n = len(arr)
        right = n - 1
        while left < right:
            if left < right and not self.check_if_alpha(arr[left]):
                left += 1
            if left < right and not self.check_if_alpha(arr[right]):
                right -= 1
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True

    def check_if_alpha(self, character):
        if (ord('A') <= ord(character) <= ord('Z') or
                ord('a') <= ord(character) <= ord('z') or
                ord('0') <= ord(character) <= ord('9')
        ):
            return True
        else:
            return False

    # Another implementation to skip elements if after ignoring certain
    # elements to check if there is a palindrome
    def is_palindrome_2(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                right -= 1
                if s[left] != s[right]:
                    return False

            if s[left] != s[right]:
                left += 1
                if s[left] != s[right]:
                    return False

            left += 1
            right -= 1

        return True

    def first_sol_is_palindrome(self, s):
        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()

        return newString == newString[::-1]
