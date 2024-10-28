"""
Given a weighted and directed graph of V vertices and edges, Find the shortest distance of all the vertex's from the source vertex, src and return a list of integers where the ith integer denotes the distance of the ith node from the source node. If a vertices can't be reach from the src then mark the distance as 108.
"""

class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellmanFord(self, V, edges, src):
        dist=[float('inf')]*V
        dist[src]=0 # distance from source to source is 0

        # we will do V-1 relaxations to get the shortest path

        for _ in range(V-1):
            for u,v,w in edges:
                # formula - dist[u]+w < dist[v] - relax the edge
                if dist[u] != float('inf') and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w # update the distance

        # check for negative cycles (if we can still relax the edges in the Vth iteration)
        for u,v,w in edges:
            if dist[u]+w<dist[v] and dist[u]!=float('inf'):
                return [-1]

        return dist
s=Solution()
V = 5
edges = [[0,1,5],[0,2,2],[2,3,3],[1,3,1],[3,4,1]]
src = 0
print(s.bellmanFord(V,edges,src)) # [0, 5, 2, 6, 7]
print()
