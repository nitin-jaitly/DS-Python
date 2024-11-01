"""

Surrounded Regions
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
123
"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
        """
        DO not return anything , modify board in place
        :param board:
        :return:
        """
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
           if (r < 0 or r == ROWS or c < 0 or c == COLS or
                   board[r][c] != "O"):
               return
           board[r][c] = "T"
           capture(r + 1, c )
           capture(r , c + 1)
           capture(r - 1, c)
           capture(r, c - 1)

        # 1. Capture Unsurrounded Regions , change 'O' -> 'T'
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0,ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        # 2. Capture Surrounded REgions , chamge all 'O's ->  'X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Uncapture Unsuroounded regions , change all 'T's -> 'O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board

def main():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "X", "O"]
    ]
    sol = Solution()

    print("Board before = \n" , board)
    print("Board after = \n", sol.solve(board))

    output_board = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "O"]
    ]
    assert output_board == sol.solve(board)


if __name__ == "__main__":
    main()