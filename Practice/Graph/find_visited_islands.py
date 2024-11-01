"""

Number of Islands
Last Updated : 17 Aug, 2024
Given a binary 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 4 islands.

Examples:

Input: M[][] = {{‘1’, ‘1’, ‘0’, ‘0’, ‘0’},
                         {‘0’, ‘1’, ‘0’, ‘0’, ‘1’},
                         {‘1’, ‘0’, ‘0’, ‘1’, ‘1’},
                        {‘0’, ‘0’, ‘0’, ‘0’, ‘0’},
                       {‘1’, ‘0’, ‘1’, ‘1’, ‘0’}}
Output: 4
Explanation: The image below shows all the 4 islands in the graph

island
Four islands in the matrix

Input: M[][] = {{‘1’, ‘1’},
                         {‘1’, ‘1’}}
Output: 1
All elements are 1, hence there is only one island

Input: M[][] = {{‘0’, ‘0’},
                         {‘0’, ‘0’}}
Output: 0
All elements are 0, hence no islands.
"""



# Python Program to find the number of islands
# using DFS with additional matrix

# A function to check if a given cell (r, c)
# can be included in DFS
def is_safe(M, r, c, visited):
    ROW = len(M)
    COL = len(M[0])

    # r is in range, c is in range, value is 1 and not
    # yet visited
    return (r >= 0) and (r < ROW) and (c >= 0) and (c < COL) and \
        (M[r][c] == '1' and not visited[r][c])


def DFS(M, r, c, visited):
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
        if is_safe(M, newR, newC, visited):
            DFS(M, newR, newC, visited)


def count_islands(M):
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
                DFS(M, r, c, visited)

                # increment the island count
                count += 1
    return count


if __name__ == "__main__":
    M = [['1', '1', '0', '0', '0'],
         ['0', '1', '0', '0', '1'],
         ['1', '0', '0', '1', '1'],
         ['0', '0', '0', '0', '0'],
         ['1', '0', '1', '1', '0']]

    print(count_islands(M))