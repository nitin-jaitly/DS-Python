class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = 0
        self.left = left
        self.right = right


class BinaryTree:
    # Recursive Solution
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.inverttree(root.left)
        self.inverttree(root.right)

        return root




