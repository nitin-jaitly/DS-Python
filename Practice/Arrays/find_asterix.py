
class Solution:

    def find_no_of_stars(self,A):
        for str in A:
            no_of_stars = 0

            print(str)
            parts = str.split('*')
            print(parts)

            for part in parts:
                if part != '':
                    print(part)

            # for i, c in enumerate(str):
            #     if c == '*':
            #         no_of_stars += 1
            # print(f"{str} {no_of_stars}")
            #
            # if no_of_stars == 1:
            #     if str[0] == '*':
            #         str_to_check = str[1:]
            #         print("STR to check = ", str_to_check)
            #     elif str[-1] == '*':
            #         str_to_check = str[:-1]
            #         print("STR to check = ", str_to_check)
            #     else:
            #         pos_of_str = str.index('*')
            #         print(pos_of_str)
            #         list_str_to_check = [str[0:pos_of_str], str[pos_of_str+1:]]
            #         print("LIST STR to CHECK = ", list_str_to_check)


def main():
    A = ["*thisstringhastwostars*",
         "*thisstringhasonestarinthebeginning",
         "thisstringhasonestarinheend*",
         "thisstringhas*onestarinthecenter",
         "this*string*has*multiple*stars*"
        ]

    sol = Solution()
    sol.find_no_of_stars(A)

if __name__ == "__main__":
    main()