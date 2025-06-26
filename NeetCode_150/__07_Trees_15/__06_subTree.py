
from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode
class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: ## Base Case If both trees are empty hence return true
            return True

        ## If either P is null or Q is not or if the data in P and Q node are not equal
        ## then return False
        if not p or not q or p.data != q.data:
            return False

        if p and q and p.data == q.data: ##
            return (self.same_tree(p.left, q.left) and
                    self.same_tree(p.right, q.right))

        return False

    def subTree(self,s : TreeNode, t: TreeNode) -> bool:

        if not t:
            return True
        if not s:
            return False

        if self.same_tree(s, t):
            return True

        return (self.subTree(s.left, t) or
                self.subTree(s.right,t))
