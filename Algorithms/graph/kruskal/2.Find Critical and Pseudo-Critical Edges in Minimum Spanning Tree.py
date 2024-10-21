"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

"""

class UnionFind:
    def __init__(self):
        self.parent = {}


    def find(self,x:int)->int:
        self.parent.setdefault(x,x)

        if x !=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,x:int,y:int)->None:
        self.parent[self.find(x)] = self.find(y)

    def is_connected(self,x:int,y:int)->bool:
        return self.find(x) == self.find(y)


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):

        for i ,edge in enumerate(edges): 
            edge.append(i) # add the index of the edge [v1,v2,weight,index]

        edges.sort(key=lambda x:x[2]) # sort the edges by weight



        # get the weight of the minimum spanning tree
        def kruskal(ignored_edge=None,forced_edge=None):
            uf= UnionFind()
            mst_weight = 0
            edges_count = 0

            # if there is forced edge add it to the mst
            if forced_edge:
                n1,n2,weight,index = forced_edge
                uf.union(n1,n2)
                mst_weight += weight
                edges_count += 1

            for n1,n2,weight,index in edges:
                if index == ignored_edge:
                    continue

                if not uf.is_connected(n1,n2):
                    uf.union(n1,n2)
                    mst_weight += weight
                    edges_count += 1

            return mst_weight if edges_count == n-1 else float('inf')

        mst_weight = kruskal()

        critical = []
        pseudo_critical = []

        for n1,n2,e_weight,index in edges:
            # try to remove the edge and check if the mst weight is increased
            if kruskal(index) > mst_weight:
                critical.append(index)
            # check if the edge is pseudo critical
            elif kruskal(None,[n1,n2,e_weight,index]) == mst_weight:
                pseudo_critical.append(index)


        return [critical,pseudo_critical]
            

# Time complexity : O(E^2logE) where E is the number of edges
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges

print("TEST CASE")
n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

print(Solution().findCriticalAndPseudoCriticalEdges(n,edges)) # [[0, 1], [2, 3, 4, 5]]
