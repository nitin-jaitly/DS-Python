from typing import List
"""
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7


"""
class Solution:
    def gen_paren(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append((s))
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        print(res)
        return res


def main():
    sol = Solution()
    n = 3
    sol.gen_paren(n)
if __name__ == "__main__":
    main()