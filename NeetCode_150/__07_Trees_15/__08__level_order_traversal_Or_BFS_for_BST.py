import collections


class TreeNode:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_length = len(q)
            level = []
            for i in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res