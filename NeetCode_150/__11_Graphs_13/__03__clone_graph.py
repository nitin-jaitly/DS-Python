class Node:
    def __init__(self,val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = None(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

