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


def driver_check_palindrome():
    string = "“M a    ; _ d    ;;  — A m"
    string = "N I TIN"
    string = string.lower()
    #string = "NITIN"
    print("The string " + string + " is a Palindrome ? " + str(check_palindrome(string)))


def check_palindrome(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        if not check_if_alpha(arr[left]):
            left += 1

        if not check_if_alpha(arr[right]):
            right -= 1

        if arr[left] != arr[right]:
            return False
        right -= 1
        left += 1
    return True


def check_if_alpha(character):
    if (
        ord('A') <= ord(character) <= ord('Z') or
        ord('a') <= ord(character) <= ord('z') or
        ord('0') <= ord(character) <= ord('9')
    ):
        return True
    else:
        return False
