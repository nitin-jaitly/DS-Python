def inOrder(TreeNode):
    if TreeNode is None:
        return
    inOrder(TreeNode.left)
    print(TreeNode.data)
    inOrder(TreeNode.right)


def preOrder(TreeNode):
    if TreeNode is None:
        return
    print(TreeNode.data)
    preOrder(TreeNode.left)
    preOrder(TreeNode.right)


def postOrder(TreeNode):
    if TreeNode is None:
        return
    postOrder(TreeNode.left)
    postOrder(TreeNode.right)
    print(TreeNode.data)

