

def DFS_Graph(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        DFS_Graph(graph, next, visited)

    return visited


def BFS_Graph(graph, start):
    visited = set()
    queue = [start]

    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex)

        for next in graph[vertex] - visited:
            visited.add(next)
            queue.append(next)

    return visited
