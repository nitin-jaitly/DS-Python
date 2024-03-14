
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class TreeTraversal:

    def preorder_traversal(self, root: TreeNode) -> list(int):
        if not root:
            return
        res = list
        res.append(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
        return res


    def inorder_traversal(self, root: TreeNode) -> list(int):
        if not root:
            return
        res = []
        inorder_traversal(root.left)
        res.append(root.val)
        inorder_traversal(root.right)
        return res


    def postorder_traversal(self, root:TreeNode) -> list(int):
        if not root:
            return
        res = []
        postoder_traversal(root.left)
        postorder_traversal(root.right)
        res.append(root.val)
        return res
