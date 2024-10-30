class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x)

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

import heapq
def minimum_spanning_tree(n: int, edges: list) -> int:
    minHeap = []
    for n1,n2,w in edges:
        heapq.heappush(minHeap,(w,n1,n2))

    uf = UnionFind()

    mst=[]

    while len(mst) < n-1:
        w,n1,n2 = heapq.heappop(minHeap)

        if not uf.is_connected(n1,n2):
            uf.union(n1,n2)
            mst.append(w)

    return sum(mst)

# Time complexity : O(ElogE) where E is the number of edges
# Space complexity : O(V+E) where V is the number of vertices and E is the number of edges
print(minimum_spanning_tree(4,[[0,1,1],[0,2,2],[0,3,3],[1,2,4],[1,3,5],[2,3,6]])) # 10
