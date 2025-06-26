
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

#from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):

    diameter = 0

    node = TreeNode()
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        diameter = max(diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return diameter

def driver_diameter_of_binary_tree():
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(diameterOfBinaryTree(root1))  # Output: 3



def main():
    driver_diameter_of_binary_tree()

if __name__ == "__main__":
    main()