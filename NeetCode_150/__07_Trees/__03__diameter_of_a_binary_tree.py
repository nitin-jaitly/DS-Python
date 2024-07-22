
""""
543. Diameter of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""

from NeetCode_150.__07_Trees.__TreeNode__ import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:

        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)
            #diameter = 2 + left + right
            height = 1 + max(left, right)
            return height
        print(type(root))
        dfs(root)
        return res[0]


    def driver_diameter_of_binary_tree(self):

        root = [1, 2, 3, 4, 5]
        print(self.diameterOfBinaryTree(root))
        #path[4, 2, 1, 3] or [5, 2, 1, 3].


