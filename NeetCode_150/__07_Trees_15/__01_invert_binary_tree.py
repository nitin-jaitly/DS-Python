
from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        #Swap children
        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root