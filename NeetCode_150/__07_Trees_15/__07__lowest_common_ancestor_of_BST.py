

from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p : 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
