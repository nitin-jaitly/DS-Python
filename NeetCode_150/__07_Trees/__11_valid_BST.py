
from NeetCode_150.__07_Trees.__TreeNode__ import TreeNode

class Solution:
    def isValid_BST(self, root:TreeNode) -> bool:
        def validTree(node, left, right):
            if not node:
                return True

            if (node.val < right  and node.val > left):
                return False
            else:
                return True

            return (
                    validTree(node.left,    left,       node.val) and
                    validTree(node.right,   node.val,   right)
                    )

        return validTree(root, float("-inf"), float("inf"))

    def driver_valid_BST(self):
        pass
