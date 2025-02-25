"""


Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
123
"""
class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        closeToOpen = {")" : "(",
                       "]" : "[",
                       "}" : "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

    def driver_valid_parenthesis(self):
        s = "()"
        if self.isValid(s):
            print("PASS")
        else:
            print("FAIL")

        s = "()[]{}"
        if self.isValid(s):
            print("PASS")
        else:
            print("FAIL")

        s = "(]"
        if self.isValid(s):
            print("PASS")
        else:
            print("FAIL")


def main():
    sol = Solution()
    sol.driver_valid_parenthesis()

if __name__== "__main__":
    main()