
from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode
class Solution:
    def same_tree(self, p: TreeNode , q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.data != q.data:
            return False

        if p and q and p.data == q.data:
            return (self.same_tree(p.left, q.right) and
                self.same_tree(p.right, q.right))

        return False
