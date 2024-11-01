"""
Etched interview , find dir size and file size


"""


import os

class FileNode:
    def __init__(self, name, size=0, is_dir=False):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def build_tree(directory):
    root = FileNode(name=directory, is_dir=True)
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            child_dir = build_tree(path)
            root.add_child(child_dir)
        else:
            size = os.path.getsize(path)
            root.add_child(FileNode(name=item, size=size))
            root.size += size
    return root

def calculate_dir_size(node):
    if node.is_dir:
        node.size = sum(calculate_dir_size(child) for child in node.children)
    return node.size

def print_tree(node, level=0):
    indent = ' ' * (4 * level)
    if node.is_dir:
        print(f"{indent}[DIR] {node.name} - {node.size} bytes")
    else:
        print(f"{indent}[FILE] {node.name} - {node.size} bytes")
    for child in node.children:
        print_tree(child, level + 1)

root_directory = '/Users/nitin/PycharmProjects/DS-Python'
root_node = build_tree(root_directory)
calculate_dir_size(root_node)
print_tree(root_node)
