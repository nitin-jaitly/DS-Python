from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s: str, open_count: int, close_count: int):
            # if the string length is 2 * n then it is a valid combination
            if len(s) == 2 * n:
                result.append(s)
                return

            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)

            # Add close parenthesis if we have more open than close
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result


def main():
    sol = Solution()
    n = 5
    sol_list = sol.generateParenthesis(n)
    print(f"sol_list is {sol_list}")

if __name__ == "__main__":
    main()