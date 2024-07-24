
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left
    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right
    def find_largest(self , root_node):
        if root_node.right:
            return self.find_largest(root_node.right)
        return root_node.value

