class TreeNode:
    def __init__(self,val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def insert_level_order(arr ,root, i, n):
    if i < n and arr[i] is not None:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root
    # if TreeNode is None:
    #     return
    # inOrder(TreeNode.left)
    # print(TreeNode.data)
    # inOrder(TreeNode.right)

def inOrder_traversal(root):
    if root is None:
        return []
    return inOrder_traversal(root.left) + [root.val] +  inOrder_traversal(root.right)

def preOrder_traversal(root):
    if root is None:
        return []
    return [root.val] + preOrder_traversal(root.left) + preOrder_traversal(root.right)
# def preOrder(TreeNode):
#     if TreeNode is None:
#         return
#     print(TreeNode.data)
#     preOrder(TreeNode.left)
#     preOrder(TreeNode.right)

def postOrder_traversal(root):
    if root is None:
        return []
    return postOrder_traversal(root.left) + postOrder_traversal(root.right) + [root.val]
# def postOrder(TreeNode):
#     if TreeNode is None:
#         return
#     postOrder(TreeNode.left)
#     postOrder(TreeNode.right)
#     print(TreeNode.data)

def main():
    #Createing a simple Binary Tree Node
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    arr = [1, 2, 3, 4, 5, 6, 7]
    root = insert_level_order(arr, None, 0, len(arr))

    print(f"{'arr':<30} {arr}")
    print(f"{'Inorder Traversal':<30} {inOrder_traversal(root)}")
    print(f"{'Preorder Traversal':<30} {preOrder_traversal(root)}")
    print(f"{'Postorder Traversal':<30} {postOrder_traversal(root)}")



if __name__ == "__main__":
    main()
