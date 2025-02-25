
"""

Given a string A = "Today is a great day" reverse words in a string with output
"day great a is Today"
"""

class Solution:
    def rev_words(self,A: list) -> list:
        stack = []
        for word in A.split():
            print(word)
            stack.append(word)
        print(stack)
        reversed_words = []
        while stack:
             reversed_words.append(stack.pop())
             print(reversed_words)

        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence

    def driver_rev_words(self):
        A = "Today is a Great day"
        print(self.rev_words(A))

def main():
    sol = Solution()
    sol.driver_rev_words()


if __name__ == "__main__":
    main()