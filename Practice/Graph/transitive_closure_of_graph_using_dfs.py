"""
Transitive Closure of a Graph using DFS
Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) in the given graph. Here reachable means that there is a path from vertex u to v. The reach-ability matrix is called transitive closure of a graph.

For example, consider below graph:


Untitled-Diagram-(1)
Graph

Transitive closure of above graphs is
1 1 1 1
1 1 1 1
1 1 1 1
0 0 0 1
"""

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        # No of Vertices
        self.V = vertices

        # default dict to store Graph
        self.graph = defaultdict(list)

        #To store transitive closure
        self.tc = [[ 0 for j in range(self.V)] for i in range(self.V)]

    ## Function to add a edge to a graph
    def addEdge(self, u,v):
        self.graph[u].append(v)


    ## A recursive DFS traversal function that finds
    # all reacheable vertices for s
    def DFSUtil(self, s, v):

        ## Mark reachability from s to v
        if (s == v):
            if ( v in self.graph[s]):
                self.tc[s][v] = 1
        else:
            self.tc[s][v] = 1
        #
        # ## Find all vertices reachable through v
        # for i in self.graph[v]:
        #


