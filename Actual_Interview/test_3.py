#
# 1. Identify whether given characters form a palindrome.
# for eg:   input: aamsm
#     a  m  s  m  a
#
#     m  a  s  a  m
#
# a - 2
# m - 2
# s - 1
#
# Input String =
#  a a s s

#  // Case if each character is an even length // We know its a palindrome .
#  // Case all other character is an even length and 1 character is an odd length  // We know its a palindrome
#

def check_palin(my_str):

    my_hash = {}
    # a : 2
    # s : 2
    for c in my_str:
        if c not in my_hash.keys():
            my_hash[c] += 1

    ## check if all keys are even length
    for k, v in my_hash.items():
        if v % 2 != 0:
            return False

    odd_count , even_count = 0,0

    ## check if one char has length as odd , rest of the chars are even
    ## check if one key has value 1 , and the rest of keys are even
    for k, v in my_hash.items():
        if v == 1:
            odd_count += 1
        if v % 2 == 0:
            even_count += 1
    l = len(my_hash.keys())
    if odd_count == 1 and even_count == l - 1:
        return True



def main():
    my_str = "aamsm"
    print(check_palin(my_str))

if __name__ == "__main__":
    main()


#          aa m s m yes ..
# s - 1 , a - 2 , m - 2 ..        m a m a m   /// mamam  , mamam


# 2. Sort and remove duplicate elements from an array
# for eg:
#         input={1,2,7,4,3,2,1,8,9}
#         ouptut={1,2,3,4,7,8,9}, length=