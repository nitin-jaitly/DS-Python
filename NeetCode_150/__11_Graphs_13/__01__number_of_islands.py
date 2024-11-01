import collections
from typing import List

class Solution:
    def numOfIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        isIslands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    r, c = row + dr , col + dc
                    if (
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visited
                        ):
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    isIslands += 1

        return isIslands


    # def numofIslands2(self, ):
    #
    #     # Python Program to find the number of islands
    #     # using DFS with additional matrix
    #
    #     # A function to check if a given cell (r, c)
    #     # can be included in DFS
    def is_safe(self, M, r, c, visited):
        ROW = len(M)
        COL = len(M[0])

        # r is in range, c is in range, value is 1 and not
        # yet visited
        return (r >= 0) and (r < ROW) and (c >= 0) and (c < COL) and \
            (M[r][c] == '1' and not visited[r][c])

    def DFS(self, M, r, c, visited):

        # These lists are used to get r and c numbers of 8
        # neighbours of a given cell
        rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[r][c] = True

        # Recur for all connected neighbours
        for k in range(8):
            newR = r + rNbr[k]
            newC = c + cNbr[k]
            if self.is_safe(M, newR, newC, visited):
                self.DFS(M, newR, newC, visited)

    def count_islands(self, M):
        ROW = len(M)
        COL = len(M[0])

        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        # Initialize count as 0 and traverse through
        # all cells of the given matrix
        count = 0
        for r in range(ROW):
            for c in range(COL):

                # If a cell with value 1 is not visited yet,
                # then a new island is found
                if M[r][c] == '1' and not visited[r][c]:
                    # Visit all cells in this island.
                    self.DFS(M, r, c, visited)

                    # increment the island count
                    count += 1
        return count


def main():
    M = [ ['1', '1', '0', '0', '0'],
          ['0', '1', '0', '0', '1'],
          ['1', '0', '0', '1', '1'],
          ['0', '0', '0', '0', '0'],
          ['1', '0', '1', '1', '0'] ]

    sol = Solution()
    print(sol.numOfIslands(M))
    print(sol.count_islands(M))

    print()
    print()

    M = [['1', '1', '0', '0', '0'],
         ['0', '1', '0', '0', '1'],
         ['1', '0', '0', '1', '1'],
         ['0', '0', '0', '0', '0'],
         ['1', '0', '1', '1', '0']]

    print(sol.count_islands(M))




if __name__ == "__main__":
    main()
