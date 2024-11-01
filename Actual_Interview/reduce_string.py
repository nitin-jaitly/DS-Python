
"""
Given a number 9 create a string
"aaaaaaaa" and reduce it to "bbbba" then reduce it to "cca" , then to "da"
"""
class Solution:
    def reduce_string(self, s):
        sol = ""
        print()

        i = 0
        print("input = ", s)
        for i in range(0, len(s) - 1, 2):
            if s[i] == s[i + 1]:
                # Find next ord value and append to solution
                next_ord_char = chr(ord(s[i]) + 1)
                sol += next_ord_char
            else:
                # append s[i] to solution
                sol += s[-1]

        if len(s) % 2 != 0:
            sol += s[-1]

        if len(list(set(s))) == len(s):
            print("s  = ", s)
            return s
        else:
            print("sol = ", sol)
            self.reduce_string(sol)

def main():
    sol = Solution()

    N = 9
    s = N * "a"
    print("ANS = ",  sol.reduce_string(s))



if __name__ == "__main__":
    main()