


from NeetCode_150.__07_Trees_15.__TreeNode__ import TreeNode

class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left) , dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1] <= 1))

            return [balanced, 1 + max(left[1], right[1]) ]

        return dfs(root)[0]


    def driver_isBalanced(self):
        root = [1, 2, 2, 3, 3, None, None, 4, 4]
        print(self.isBalanced(root))