import collections
from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view_of_BST(self, root:TreeNode) -> list[int]:

        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLength = len(q)

            for i in range(qLength):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res