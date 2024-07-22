from collections import deque


from NeetCode_150.__07_Trees.__TreeNode__ import TreeNode

class Solution:
    ## Using recursions
    def max_depth(self,root:TreeNode):
        if not root:
            return 0
        return 1 + self.max_depth(self.max_depth(root.left), self.max_depth(root.right))

    def max_depth_bfs(self, root:TreeNode):
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level


    def max_depth_iterative_dfs(self, root:TreeNode):
        stack = [root, 1]
        res = 0
        while stack:
            root, depth = stack.pop()

            if root:
                res = max(res, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])
        return res

