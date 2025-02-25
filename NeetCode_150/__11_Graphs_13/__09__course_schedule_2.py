"""


Course Schedule II
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
123
"""
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = { c : [] for c in range(numCourses) }
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        # a course has 3 possible states

        # visited -> crs has been added to output

        # visiting -> crs not added to output, but added to cycle

        # unvisited -> crs not added to output or cycle

        output = []
        visit , cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

def main():
    sol = Solution()
    numCourses = 3
    prerequisites = [[1, 0]]
    output = [0, 1, 2]

    assert output == sol.findOrder(numCourses, prerequisites)

    numCourses = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    output = []
    assert output == sol.findOrder(numCourses, prerequisites)

if __name__ == "__main__":
    main()